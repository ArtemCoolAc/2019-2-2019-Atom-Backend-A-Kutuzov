from django.db import models
from user_profile.models import User
import json


class Chat(models.Model):
    title = models.CharField(max_length=128, default='Чат')
    is_group_chat = models.BooleanField(default=False)
    topic = models.CharField(max_length=100, default='')
    last_message = models.TextField(default='')
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def to_json(self):
        return json.dumps({'title': self.title,
                           'is_group_chat': self.is_group_chat,
                           'topic': self.topic,
                           'last_message': self.last_message,
                           'creator': self.creator.to_json()}, ensure_ascii=False)

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"

# Create your models here.
