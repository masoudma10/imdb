from celery import shared_task
from django.core.mail import send_mail
from users.models import User

@shared_task
def send_email_task(movie, description):
    user = User.objects.all()
    send_mail('new movie on imdb!',
              f'name:{movie}\n description:{description}',
              'masoud.mohebali10@gmail.com',
              [email for email in user],)

    return True