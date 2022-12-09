# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Get the user id from the scope
        # self.user_id = self.scope['user'].id

        # Get the other user id from the URL route
        self.other_user_id = self.scope['url_route']['kwargs']['other_user_id']

        # here room_name is other user id/name got from url
        # self.room_name = self.scope["url_route"]["kwargs"]["room_name"]


        # Create a group for the chat, to do 
        # self.chat_group_name = 'chat_%s_%s' % (user_id, other_user_id)

        self.chat_group_name = "chat_%s" % self.other_user_id

        # Join room group
        await self.channel_layer.group_add(self.chat_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.chat_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.chat_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))