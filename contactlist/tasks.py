import celery


@celery.shared_task
def send_welcome_email():
    pass  # long running task
