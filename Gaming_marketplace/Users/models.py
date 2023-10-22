from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    password = models.IntegerField(max_length=200)