from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class User(AbstractUser):
	def has_related_object(self):
		try:
			self.user
			return True
		except ObjectDoesNotExist:
			return False

    
# Create your models here.
class loc(models.Model):
	lon = models.FloatField(null=True, blank=True, default=None)
	lat = models.FloatField(null=True, blank=True, default=None)
	user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="user", primary_key=True)

