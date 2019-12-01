from django.db import models

class Sticker(models.Model):
	name = models.CharField(max_length=32, null=true)
# Create your models here.
