from django.contrib import admin

from contactlist import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
