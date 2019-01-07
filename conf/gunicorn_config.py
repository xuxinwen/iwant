# -*- coding: utf-8 -*-
import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count()
worker_class = 'gevent'

BASE_PATH = '/app/juno'
django_settings = 'juno.settings'

max_requests = 5000
timeout = 300

user = 'root'
group = 'root'

pidfile = '/tmp/vfine-gunicorn.pid'
errorlog = '/var/log/gunicorn/stderr.log'
