# Generated by Django 2.2.5 on 2019-10-30 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nick',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
