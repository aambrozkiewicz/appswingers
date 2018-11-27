from django.conf import settings
from django.db import models
from django import forms


class CustomAgeField(models.PositiveIntegerField):
    def to_python(self, value):
        return super().to_python(value)

    def formfield(self, **kwargs):
        defaults = {
            **kwargs,
            'form_class': forms.ChoiceField,
        }
        return super().formfield(**defaults)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    age = CustomAgeField(choices=((1, 'Raz'),))
    email = models.EmailField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='contacts',
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.phone_number}'


class Address(models.Model):
    TYPES = (
        ('home', 'Home'),
        ('work', 'Work'),
    )

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,
                                related_name='addresses')
    address_type = models.CharField(max_length=32, choices=TYPES)
    street = models.CharField(max_length=255)
    post_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.contact.name} {self.address_type}'
