from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ()
        extra_kwargs = {
            "to": {
                "required": False
            },
            "user": {
                "required": False
            }
        }

    def save(self, **kwargs):
        print(self.context)
        return super().save(**kwargs)
