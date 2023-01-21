from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task()
def send_mail_func(task_id):
    from task.models import Task
    #operations
    task = Task.objects.get(id = task_id)
    
    if task.executed:
        mail_subject="Task {0} completed".format(task.title)
        message="I have completed '{0}' task by celery!".format(task.title)
    else:
        mail_subject="Task {0} canceled".format(task.title)
        message="i canceled the task '{0}' by celery!".format(task.title)
    to_email=task.owner.email
    send_mail(
        subject = mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )
    return "Done"
