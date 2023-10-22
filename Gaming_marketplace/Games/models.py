from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(max_length=50)
    creator = models.TextField(max_length=50)
    genre = models.TextField(max_length=150)
    year = models.IntegerField(max_length=20)