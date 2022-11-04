from django.db import models

# Create your models here.
class loc(models.Model):
	lon = models.FloatField(null=True, blank=True, default=None)
	lat = models.FloatField(null=True, blank=True, default=None)


