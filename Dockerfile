FROM ubuntu:18.04
MAINTAINER 'xinwen' coderWen@126.com
WORKDIR /app

EXPOSE 80
ENV TERM xterm

# 阿里源
COPY conf/sources.list /etc/apt/sources.list

# 豆瓣源 COPY命令中不能使用`~`定位主目录
COPY conf/pip.conf /root/.pip/pip.conf

# * `python3-pip` 自带 `python3.6`
RUN deps='nginx python3-pip supervisor wget vim sqlite3 cron'; \
    set -x \
    && apt-get update && apt-get install -y $deps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install -r requirements.txt

# 常变化区
COPY . /app

CMD ["gunicorn iwant.wsgi --bind=80"]

# Docker 上线前要先测试下新镜像。
