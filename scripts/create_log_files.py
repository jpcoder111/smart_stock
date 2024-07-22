import os

log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../logs/http_requests')
os.makedirs(log_dir, exist_ok=True)

request_log = os.path.join(log_dir, 'requests.log')
response_log = os.path.join(log_dir, 'responses.log')

with open(request_log, 'a'):
    os.utime(request_log, None)

with open(response_log, 'a'):
    os.utime(response_log, None)
