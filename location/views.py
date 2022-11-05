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


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if request.method == "POST":
        la = request.POST.get('lat')
        lo = request.POST.get('lon')

        loc.objects.get_or_create(
        lat=la,
        lon=lo,
        user= request.user
)
    return render(request, "index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html",{"messege":"Invalid Credentials."})
    else: 	
        return render(request, "login.html")


def logout_view(request):
	logout(request)
	return render(request, "login.html", {"messege":"LOGGED OUT"})


def locDetails(request):
    u = request.user
    uid = u.user.get().id
    loca = loc.objects.get(pk=uid)
    return render(request,"locDetails.html",{'l':loca})