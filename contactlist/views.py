from rest_framework import viewsets, permissions

from contactlist import models, serializers


class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ContactSerializer

    def get_queryset(self):
        return models.Contact.objects.filter(
            user=self.request.user,
        )
