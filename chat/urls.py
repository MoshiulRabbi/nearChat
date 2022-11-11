from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat, name = "chat" ),
    path('<str:username>', views.chatPage, name = "chatPage" )
]
