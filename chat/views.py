from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from location.views import findClosestFun
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Message

# Create your views here.
def chat(request):
    allu = get_user_model()
    authUser = allu.objects.exclude(username=request.user.username)
    return render(request,"chat/chatIndex.html",{"allu":authUser})


def chatPage(request,username):
    other_user = User.objects.get(username=username) #to show the name
    # allu = get_user_model()
    # authUser = allu.objects.exclude(username=request.user.username)

    if request.user.id > other_user.id:
        thread_name = f'chat_{request.user.id}-{other_user.id}'
    else:
        thread_name = f'chat_{other_user.id}-{request.user.id}'

    message_objs = Message.objects.filter(thread_name=thread_name)

    closestUser = findClosestFun(request)
    return render(request,"chat/chatPage.html",{"closestUser":closestUser,
    "other_user":other_user,"username":username,"message":message_objs})