import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# logger = logging.getLogger('webhook')

@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "DELETE", "PATCH"])
def universal_listener(request):
    return JsonResponse({'success': True,
                         'message': 'Webhook received successfully!'})