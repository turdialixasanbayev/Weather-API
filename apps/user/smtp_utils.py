from django.core.mail import send_mail
from django.conf import settings

def send_notification_email(to, subject, message):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to],
        fail_silently=False
    )
