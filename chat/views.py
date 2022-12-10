from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from location.views import findClosestFun
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Message
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def chat(request):
    closest_users = findClosestFun(request)
    return render(request, 'chat/chatIndex.html', {'closest_users': closest_users})

@login_required
def chatPage(request,username):
    other_user = User.objects.get(username=username) #to show the name

    #todo
    # thread_name = (''.join(set(request.user.username + other_user)))

    if request.user.id > other_user.id:
        thread_name = f'chat_{request.user.id}-{other_user.id}'
    else:
        thread_name = f'chat_{other_user.id}-{request.user.id}'
    message_objs = Message.objects.filter(thread_name=thread_name)

    closestUser = findClosestFun(request)
    return render(request,"chat/chatPage.html",{"closestUser":closestUser,
    "other_user":other_user,"username":username,"message":message_objs})