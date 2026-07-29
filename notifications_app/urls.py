from django.urls import path
from .views import BulkNotificationAPIView

urlpatterns = [
    path('notifications/bulk/', BulkNotificationAPIView.as_view(), name='bulk-notifications'),
]