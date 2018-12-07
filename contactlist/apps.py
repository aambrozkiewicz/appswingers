from django.apps import AppConfig


class ContactlistConfig(AppConfig):
    name = 'contactlist'

    def ready(self):
        from . import signals  # noqa
