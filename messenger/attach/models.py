from django.db import models
from chats.models import Chat
from user_profile.models import User
from message.models import Message


class Attachment(models.Model):
    chat = models.ForeignKey(Chat, related_name='%(class)s_chat', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, related_name='%(class)s_user', on_delete=models.SET_NULL, null=True)
    message = models.ForeignKey(Message, related_name='%(class)s_message', on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=50, default='')
    url = models.URLField(null=True)

    class Meta:
        verbose_name = "Прикрепление",
        verbose_name_plural = "Прикрепления"
# Create your models here.
