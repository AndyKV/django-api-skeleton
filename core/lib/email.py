from django.core.mail import send_mail as django_send_mail


def send_mail(*args, **kwargs):
    return django_send_mail(*args, **kwargs)
