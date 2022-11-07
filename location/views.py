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

def locDetails(request):
    u = request.user
    if u.has_related_object():
        uid = u.id
        loca = loc.objects.get(pk=uid)
     
        allu = get_user_model().objects.all()

        #get lat/lon of all users
        allLoc = loc.objects.values_list('lat','lon')

        #get current users lat/lon
        userLocation = (loca.lat,loca.lon)

        #get allCoor without users coor
        allLoc = allLoc.exclude(lat=loca.lat)
        
        #ranges
        ranges = 2
        cu = closestUser(allLoc,userLocation,ranges)

        #get users of closest location

        al = loc.objects.all()

        objectDict = {}
        for i in cu:
            a = al[i]
            value=a.user
            key=a.user.username
            objectDict[key]=value

            
        return render(request,"locDetails.html",{'l':loca,"allu":allu,'ll':allLoc,'test':cu,"un":objectDict})
    else:
        m = 'Please turn on GPS'
        return render(request,"locDetails.html",{'m':m})



def sta(request):
    allu = get_user_model().objects.all()
    return render(request,"sta.html",{"allu":allu})