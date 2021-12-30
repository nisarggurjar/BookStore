from celery import shared_task
from django.conf import settings
from django.core.mail import send_mass_mail
#from DRFPro.emails import emails
emails = ['nisarggurjar16@gmail.com']
@shared_task(bind = True)
def test_func(self):
    for i in range(20):
        print(i)
    return "Done"

@shared_task
def send_emails(subject, message):
    mail = (subject, message, settings.EMAIL_HOST_USER, emails)
    send_mass_mail((mail,), fail_silently=False)
    return "Done"