# gunicorn_config.py

def on_starting(server):
    workers = server.app.cfg.settings['workers'].value
    bind = server.app.cfg.settings['bind'].value
    if isinstance(bind, list):
        bind = bind[0]
    host, port = bind.split(':')
    print(f"🚀 Gunicorn is starting up...")
    print(f"🔧 Number of workers: {workers}")
    print(f"🌐 Binding to: {host}:{port}")

def post_fork(_, worker):
    worker_id = worker.pid
    print(f"🔧 Worker {worker_id} has been forked.")

bind = '0.0.0.0:8000'
workers = 3
accesslog = None
errorlog = None
loglevel = 'info'

# Adding the hooks
on_starting = on_starting
post_fork = post_fork
