from rest_framework import serializers

from contactlist import models


class ContactSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Contact
        fields = ('pk', 'name', 'phone', 'age', 'user',)
