# Generated by Django 4.1.3 on 2022-11-12 14:58

import chat.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(blank=True, max_length=500)),
                ('is_close', models.BooleanField(default=False)),
                ('distributor_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1_rooms', to=settings.AUTH_USER_MODEL)),
                ('shop_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2_rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_reply', models.BooleanField(default=False)),
                ('message', models.CharField(max_length=800)),
                ('reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reply_to_message', to='chat.message')),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_messages', to='chat.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChatProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=30, unique=True)),
                ('image', imagekit.models.fields.ProcessedImageField(default='default/img.jpg', max_length=255, upload_to=chat.models.ChatProfile.user_dir)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_chat_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
