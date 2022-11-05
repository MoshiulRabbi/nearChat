from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(loc)

from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = User
admin.site.register(User, CustomUserAdmin)