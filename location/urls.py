from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index" ),
    path("login",views.login_view, name = "login"),
    path("logout", views.logout_view, name = "logout" ),
    path("locDetails/", views.locDetails, name = "locDetails" ),
    path("chat/", views.chat, name = "chat" ),
    path('<str:username>', views.chatPage, name = "chatPage" )
]
