from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_mail_celery


def index(request):
    send_mail_celery.delay()
    return HttpResponse("hello")
