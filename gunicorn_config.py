# gunicorn_config.py

bind = '0.0.0.0:8000'
workers = 3
accesslog = './logs/access.log'
errorlog = './logs/error.log'
loglevel = 'info'