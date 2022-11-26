from django.urls import path

from chat.cosumers import ChatConsumer

app_name = "chat"

ws_urlpatterns = [
    path(r'ws/chat/<str:channel_name>/', ChatConsumer.as_asgi(), name='chat_consumer')
]
