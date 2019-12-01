# Generated by Django 2.2.5 on 2019-10-28 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_profile', '0001_initial'),
        ('chats', '0002_auto_20191028_2209'),
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_messages', models.CharField(default='', max_length=100)),
                ('chat_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member_chat_id', to='chats.Chat')),
                ('last_read_message_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_read_message_id', to='message.Message')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member_user_id', to='user_profile.User')),
            ],
        ),
    ]
