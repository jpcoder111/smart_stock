from django.urls import path
from .views import universal_listener

urlpatterns = [
    path('universal_listener/', universal_listener, name='universal_listener'),
]
