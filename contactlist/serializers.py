from rest_framework import serializers

from contactlist import models


class ContactSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    gender = serializers.SerializerMethodField()

    class Meta:
        model = models.Contact
        fields = ('pk', 'name', 'phone', 'age', 'user', 'gender',)

    def get_gender(self, instance):
        return 'female' if instance.name[-1] == 'a' else 'male'
