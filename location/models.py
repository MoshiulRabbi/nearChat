from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class User(AbstractUser):
	pass

    
# Create your models here.
class UserLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user")
    latitude = models.FloatField()
    longitude = models.FloatField()