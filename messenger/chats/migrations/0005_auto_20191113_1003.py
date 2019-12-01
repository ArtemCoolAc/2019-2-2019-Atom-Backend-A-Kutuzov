# Generated by Django 2.2.5 on 2019-11-13 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0004_auto_20191112_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='title',
            field=models.CharField(default='Чат', max_length=128),
        ),
        migrations.AlterField(
            model_name='chat',
            name='last_message',
            field=models.TextField(default=''),
        ),
    ]
