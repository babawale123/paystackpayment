from django.urls import path
from .views import PaystackWebhook


urlpatterns = [
    path('webhook/', PaystackWebhook.as_view(), name='paystack-webhook'),
]