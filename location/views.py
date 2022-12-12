from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
import json
import time
from .models import *
from geopy.distance import geodesic
from django.db import IntegrityError

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if request.method == "POST":
        latitude = request.POST['lat']
        longitude = request.POST['lon']
        user_location, created = UserLocation.objects.get_or_create(
            user=request.user,
            defaults={'latitude': latitude, 'longitude': longitude}
        )
        if not created:
            user_location.latitude = latitude
            user_location.longitude = longitude
            user_location.save()
    return render(request, "location/index.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "location/register.html", {
                "message": "Passwords must match."
            })

        #Check Required Field
        if username == '' or password == '' or confirmation == '':
            message="Please input data in the fields"
            return render(request, "location/register.html",{"message":message})


        # Attempt to create new user
        try:
            user = User.objects.create_user(username,email,password)
            user.save()
        except IntegrityError:
            return render(request, "location/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "location/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "location/login.html",{"messege":"Invalid Credentials."})
    else: 	
        return render(request, "location/login.html")

@login_required
def logout_view(request):
	logout(request)
	return render(request, "location/login.html", {"messege":"LOGGED OUT"})
    
@login_required
def findClosestFun(req):
    current_location = UserLocation.objects.get(user=req.user)
    user_locations = UserLocation.objects.exclude(user=req.user)
    closest_users = []
    for user_location in user_locations:
        distance = geodesic((current_location.latitude, current_location.longitude), (user_location.latitude, user_location.longitude)).km
        if distance <= 11:
            closest_users.append({'user': user_location.user, 'distance': distance})
    closest_users.sort(key=lambda x: x['distance'])
    return closest_users
