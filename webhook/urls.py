from django.urls import path
from .views import webhook_listener

urlpatterns = [
    path('listener/', webhook_listener, name='webhook_listener'),
]
