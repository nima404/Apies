from uuid import uuid5, NAMESPACE_URL

from django.db import models
from django.conf import settings
from pilkit.processors import ResizeToFill
from imagekit.models import ProcessedImageField


class ChatProfile(models.Model):
    def user_dir(self, filename: str) -> str:
        return f'{uuid5(NAMESPACE_URL, str(self.user.id))}/profile/{filename}'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_chat_profile', on_delete=models.CASCADE)
    chat_id = models.CharField(max_length=30, unique=True)
    image = ProcessedImageField(upload_to=user_dir, max_length=255, default='default/img.jpg',
                                processors=[ResizeToFill(500, 500)], format='JPEG', options={'quality': 50})

    def __str__(self):
        return self.user.id


class Room(models.Model):
    def make_room_number(self):
        return uuid5(NAMESPACE_URL, self.id).hex

    room_number = models.CharField(max_length=500, blank=True)
    distributor_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user1_rooms', on_delete=models.CASCADE)
    shop_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user2_rooms', on_delete=models.CASCADE)

    is_close = models.BooleanField(default=False)

    def __str__(self):
        return self.room_number

    def save(self, *args, **kwargs):
        self.room_number = uuid5(NAMESPACE_URL, str(self.id)).hex
        super().save(*args, **kwargs)


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_messages', on_delete=models.CASCADE)
    reply_to = models.ForeignKey('self', related_name='reply_to_message', on_delete=models.SET_NULL, null=True,
                                 blank=True)
    is_reply = models.BooleanField(default=False)
    message = models.CharField(max_length=800)
    to = models.ForeignKey(Room, related_name='room_messages', on_delete=models.CASCADE)

    def __str__(self):
        return f'FROM {self.user}: {self.message} :TO {self.to}'
