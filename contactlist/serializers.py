from rest_framework import serializers
from django.core import validators

from contactlist import models


class ContactSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()

    class Meta:
        model = models.Contact
        fields = ('pk', 'name', 'phone_number', 'age', 'email', 'gender',)
        extra_kwargs = {
            'name': {
                'validators': [
                    validators.MaxLengthValidator(10, message='Zdecydowanie za długie to imie'),
                ],
            },
        }

    def get_gender(self, instance):
        return 'female' if instance.name.endswith('a') else 'male'

    # def validate_phone_number(self, attr):
    #     return f'+48{attr}'
