from django.conf import settings
from django.db.models import signals
from django.dispatch import receiver

from contactlist import tasks


@receiver(signals.post_save, sender=settings.AUTH_USER_MODEL)
def send_user_welcome_email(sender, instance, **kwargs):
    tasks.send_user_welcome_email.delay(instance.pk)
    tasks.fetch_user_repositories.apply_async(
        args=(instance.pk,),
        # eta=timezone.now() + datetime.timedelta(days=1),
        countdown=10,
    )
