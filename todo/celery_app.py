import os
import time 

from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')
from django.conf import settings

app = Celery('todo')
app.config_from_object('django.conf.settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

# @app.task()
# def debug_task():
#     print('Hello from debug_task')