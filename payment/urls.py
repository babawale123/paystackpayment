from django.urls import path
from .views import PaystackWebhook,GetAllTransaction


urlpatterns = [
    path('', GetAllTransaction.as_view()),
    path('webhook/', PaystackWebhook.as_view(), name='paystack-webhook'),
]