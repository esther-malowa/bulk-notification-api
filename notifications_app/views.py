from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BulkNotificationSerializer


class BulkNotificationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BulkNotificationSerializer(data=request.data)

        if serializer.is_valid():
            result = serializer.save()
            sender = result['sender']
            notifications = result['notifications']

            return Response(
                {
                    "message": "Bulk notifications created successfully.",
                    "sender": {
                        "id": sender.id,
                        "name": sender.name,
                        "email": sender.email,
                    },
                    "total_notifications_created": len(notifications),
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "message": "Validation failed.",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )