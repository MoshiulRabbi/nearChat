from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserLocation)

from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
admin.site.register(User, CustomUserAdmin)