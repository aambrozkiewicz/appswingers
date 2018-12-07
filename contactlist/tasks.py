import celery
from django.contrib import auth
from django.core import mail


@celery.shared_task
def send_user_welcome_email(user_pk):
    user = auth.get_user_model().objects.get(pk=user_pk)
    mail.send_mail(
        'Welcome as contact list user!',
        'Your account is ready!',
        'noreply@apptension.com',
        [user.email],
        fail_silently=False,
    )
