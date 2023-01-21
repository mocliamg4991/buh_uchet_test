from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
from .tasks import send_mail_func 

class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    text = models.TextField()
    deadline = models.DateTimeField()
    executed = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_executed = self.executed
    
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.executed != self.__original_executed:
            # name changed - do something here
            send_mail_func.delay(self.id)
        self.__original_executed = self.executed
        return super().save(force_insert, force_update, *args, **kwargs)

    def __str__(self) -> str:
        return self.title

    