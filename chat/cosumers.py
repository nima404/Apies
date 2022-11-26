import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from .serializers import MessageSerializer
from chat.models import Room


@database_sync_to_async
def room_check(room_number):
    return Room.objects.filter(room_number=room_number)


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        if isinstance(self.scope['user'], AnonymousUser):
            await self.disconnect(1000)
        self.room_number = self.scope['url_route']['kwargs']['channel_name']
        if await room_check(self.room_number):
            self.room_group_name = f'chat_{self.room_number}'
            await self.channel_layer.group_add(
                self.room_number,
                self.room_group_name,
            )
            await self.accept()
        else:
            await self.disconnect(1000)

    async def disconnect(self, code):
        if code == 1000:
            await self.close(code)
        else:
            await self.channel_layer.group_discard(
                self.room_number,
                self.room_group_name
            )

    async def receive_json(self, content, **kwargs):
        ser = MessageSerializer(data=content)
        if ser.is_valid():
            await self.send(json.dumps({"accepted": True}))
        else:
            await self.send(json.dumps(ser.errors))
