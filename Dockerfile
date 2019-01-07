FROM ubuntu:18.04
MAINTAINER 'xinwen' coderWen@126.com
WORKDIR /app

# 重型任务区
# 阿里源[无奈脸]
COPY conf/sources.list /etc/apt/sources.list
# 豆瓣源
# COPY命令中不能使用`~`定位主目录
COPY conf/pip.conf /root/.pip/pip.conf

RUN deps='nginx python3.7 supervisor wget vim sqlite3 cron'; \
    set -x \
    && apt-get update && apt-get install -y $deps --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

EXPOSE 80

ENV TERM xterm

# 常变化区
COPY . /app

CMD ["/bin/bash"]
