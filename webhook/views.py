import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Configure logging
logger = logging.getLogger(__name__)

@csrf_exempt
def webhook_listener(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        logger.info(f"Received webhook data: {data}")
        return JsonResponse({'status': 'success12345'})
    return JsonResponse({'status': 'failure'}, status=400)
