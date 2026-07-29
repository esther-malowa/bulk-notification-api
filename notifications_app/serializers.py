from django.db import transaction
from rest_framework import serializers
from .models import Sender, Notification


class NotificationInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['title', 'message', 'channel']


class BulkNotificationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    notifications = NotificationInputSerializer(many=True, allow_empty=False)

    @transaction.atomic
    def create(self, validated_data):
        notifications_data = validated_data.pop('notifications')

        
        sender = Sender.objects.create(**validated_data)

        
        notification_instances = [
            Notification(sender=sender, **item)
            for item in notifications_data
        ]

        
        created_notifications = Notification.objects.bulk_create(notification_instances)

        return {
            'sender': sender,
            'notifications': created_notifications,
        }