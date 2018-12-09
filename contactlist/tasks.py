import celery
import requests
import smtplib
from django.contrib import auth
from django.core import mail

from contactlist import models


@celery.shared_task(
    autoretry_for=(smtplib.SMTPException,),
    retry_kwargs={'countdown': 10, 'max_retries': 3},
)
def send_user_welcome_email(user_pk):
    user = auth.get_user_model().objects.get(pk=user_pk)
    mail.send_mail(
        'Welcome as contact list user!',
        'Your account is ready!',
        'noreply@apptension.com',
        [user.email],
        fail_silently=False,
    )


@celery.shared_task()
def fetch_user_repositories(user_pk):
    user = auth.get_user_model().objects.get(pk=user_pk)
    response = requests.get(
        f'https://api.github.com/users/{user.username}/repos',
    )
    response.raise_for_status()
    json_response = response.json()
    for repo in json_response:
        models.UserGitHubRepository.objects.update_or_create(
            user=user,
            ext_id=repo['id'],
            defaults={
                'html_url': repo['html_url'],
                'name': repo['name'],
            },
        )
