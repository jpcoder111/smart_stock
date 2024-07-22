# main.middlewares.http_requests.py
import logging
import time
import uuid

request_logger = logging.getLogger('http_requests.request')
response_logger = logging.getLogger('http_requests.response')

class LogRequestResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = str(uuid.uuid4())
        start_time = time.time()

        # Log the request details
        request_logger.info({
            'event': 'request',
            'request_id': request_id,
            'method': request.method,
            'path': request.path,
            'headers': dict(request.headers),
            'query_params': dict(request.GET),
            'body': request.body.decode('utf-8') if request.body else None,
        })

        response = self.get_response(request)
        duration = time.time() - start_time

        # Log the response details
        response_logger.info({
            'event': 'response',
            'request_id': request_id,
            'status_code': response.status_code,
            'headers': dict(response.items()),
            'body': response.content.decode('utf-8') if response.content else None,
            'duration': duration,
        })

        return response
