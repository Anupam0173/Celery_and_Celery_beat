from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
import time

@shared_task
def send_mail_celery():
    print("hello")
    print("99999999999")
    return None