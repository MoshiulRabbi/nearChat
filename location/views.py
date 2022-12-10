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


def logout_view(request):
	logout(request)
	return render(request, "location/login.html", {"messege":"LOGGED OUT"})



#location function
def closestUser(Allcoor,userCoor,ranges):
    
    #find all the distance of users
    nl = []
    for i in Allcoor:
        nl.append(round(geodesic(i,userCoor).km,3))
    
    #specify certain range
    sl = []
    for i in nl:
        if i < ranges:
            sl.append(i)

    #find the index of users of certain ranges

    li = []
    for i in nl:
        for k in sl:
            li.append(nl.index(k))
        break

    #find the final user
    a = []
    for i in Allcoor:
        for k in li:
            a.append(Allcoor[k])
        break

    # remove 

    return li

# def locDetails(request):
#     u = request.user
#     if u.user.exists():
#         uid = u.user.get().id
#         loca = loc.objects.get(pk=uid)
     
#         allu = get_user_model().objects.all()

#         #get lat/lon of all users
#         allLoc = loc.objects.values_list('lat','lon')

#         #get current users lat/lon
#         userLocation = (loca.lat,loca.lon)

#         #get allCoor without users coor
#         #allLoc = allLoc.exclude(lat=loca.lat)
        
#         #ranges
#         ranges = 2
#         cu = closestUser(allLoc,userLocation,ranges)

#         #get users of closest location

#         al = loc.objects.all()

#         closestU = []

#         for i in cu:
#             closestU.append(al[i])
            
#         #filteredUser = al.filter(id__in=[al[i].id for i in cu])

#         return render(request,"location/locDetails.html",{'l':loca,"allu":allu,'ll':allLoc,'test':cu,"un":closestU})
#     else:
#         m = 'Please turn on GPS'
#         return render(request,"location/locDetails.html",{'m':m})



@login_required
def find_closest_users(request):
    current_location = UserLocation.objects.get(user=request.user)
    user_locations = UserLocation.objects.exclude(user=request.user)
    closest_users = []
    for user_location in user_locations:
        distance = geodesic((current_location.latitude, current_location.longitude), (user_location.latitude, user_location.longitude)).km
        if distance <= 11:
            closest_users.append({'user': user_location.user, 'distance': distance})
    closest_users.sort(key=lambda x: x['distance'])
    return render(request, 'location/chatIndex.html', {'closest_users': closest_users})