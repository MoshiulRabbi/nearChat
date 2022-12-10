#  path('ws/<int:id>/', PersonalChatConsumer)


# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    #user id is name for now
    re_path(r"ws/(?P<other_user_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]