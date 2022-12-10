from django.db import models
from location.models import User

# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=100, default=None)
    recipient = models.CharField(max_length=100, default=None)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self) -> str:
        return self.thread_name