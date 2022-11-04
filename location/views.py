from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
import json
import time
from .models import *


# Create your views here.
def index(request):
    if request.method == "POST":
        la = request.POST.get('lat')
        lo = request.POST.get('lon')

        l = loc(lon=lo,lat=la)
        l.save()

    return render(request,"index.html")