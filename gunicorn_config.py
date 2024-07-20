# gunicorn_config.py

bind = '0.0.0.0:8000'
workers = 3
accesslog = None
errorlog = None
loglevel = 'info'