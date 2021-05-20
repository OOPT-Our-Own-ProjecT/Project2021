from django.db import models

# Create your models here.python manage.py migrate --fake yourapp zero
class User(models.Model):
    email = models.CharField(max_length=30, primary_key=True)
    pw = models.CharField(max_length=30, null=False, default="")
    nickname= models.CharField(max_length=30, null=False, default="")
