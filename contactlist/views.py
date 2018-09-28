from rest_framework import viewsets, permissions

from contactlist import models, serializers


class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
