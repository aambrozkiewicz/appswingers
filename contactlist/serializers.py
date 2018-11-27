from rest_framework import serializers, exceptions
from django.core import validators

from contactlist import models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'

    def validate_city(self, attr):
        if attr.lower() == 'warszawa':
            raise exceptions.ValidationError('Tylko nie Warszawa')
        return attr.upper()

    def validate(self, attrs):
        if attrs['city'] == 'POZNAN' and not attrs['post_code'].startswith('61'):
            raise exceptions.ValidationError(
                detail={'post_code': 'Błędny kod pocztowy'})
        return attrs


class ContactSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    addresses = AddressSerializer(many=True, required=False)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.Contact
        fields = ('pk', 'name', 'phone_number', 'age', 'email', 'gender',
                  'addresses', 'user',)
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
