from django.db import models
from user_profile.models import User
from chats.models import Chat
from message.models import Message


class Member(models.Model):
    user = models.ForeignKey(User, related_name='%(class)s_user', on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(Chat, related_name='%(class)s_chat', on_delete=models.SET_NULL, null=True)
    new_messages = models.CharField(max_length=100, default='')
    last_read_message = models.ForeignKey(Message, related_name='last_read_message', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Участник чата',
        verbose_name_plural = 'Участники чата'
# Create your models here.
