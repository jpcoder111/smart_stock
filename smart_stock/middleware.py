# smart_stock/middleware.py
import logging

logger = logging.getLogger(__name__)

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request details
        logger.info(f"Request: {request.method} {request.path}")
        response = self.get_response(request)
        # Log the response details
        logger.info(f"Response: {response.status_code}")
        return response