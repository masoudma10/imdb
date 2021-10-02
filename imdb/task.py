from celery import shared_task
from django.core.mail import send_mail
from users.models import User
from celery.exceptions import TaskError
from .Exceptions import UserDoesNOtExists, SendMailError
from django.core.exceptions import ObjectDoesNotExist


@shared_task
def send_email_task(movie, description):

    """
    celery task for sending email
    :param movie:
    :param description:
    :return: True
    """
    try:
        user = User.objects.all()
    except UserDoesNOtExists as e:
        raise ObjectDoesNotExist(e)
    try:
        send_mail('new movie on imdb!',
                  f'name:{movie}\n description:{description}',
                  'masoud.mohebali10@gmail.com',
                  [email for email in user],)
    except SendMailError as e:
        raise TaskError(e)

    return True