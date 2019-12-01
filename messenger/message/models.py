from django.db import models
from chats.models import Chat
from user_profile.models import User


class Message(models.Model):
    user = models.ForeignKey(User, related_name='%(class)s_user', on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(Chat, related_name='%(class)s_chat', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    # added_at = models.CharField(max_length=100, null=True)
    added_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-added_at',)
        verbose_name = "Сообщение",
        verbose_name_plural = "Сообщения"
# Create your models here.
