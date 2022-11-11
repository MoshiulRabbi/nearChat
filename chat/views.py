from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
def chat(request):
    allu = get_user_model()
    authUser = allu.objects.exclude(username=request.user.username)
    return render(request,"chat/chatIndex.html",{"allu":authUser})


def chatPage(request,username):
    other_user = User.objects.get(username=username)
    allu = get_user_model()
    authUser = allu.objects.exclude(username=request.user.username)
    return render(request,"chat/chatPage.html",{"allu":authUser,"other_user":other_user})