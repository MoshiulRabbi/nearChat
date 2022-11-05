from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE


# Create your models here.
class User(AbstractUser):
    pass
# Create your models here.
class loc(models.Model):
	lon = models.FloatField(null=True, blank=True, default=None)
	lat = models.FloatField(null=True, blank=True, default=None)
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user")


