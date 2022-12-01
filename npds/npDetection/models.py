from django.db import models

# Create your models here.
class numberplate(models.Model):
    numPlate = models.CharField(max_length=20)
    colour = models.CharField(max_length=10)
    auth = models.IntegerField()

class numPlateRecords(models.Model):
    numPlate = models.CharField(max_length=20)
    auth = models.IntegerField()
    dateAndTime = models.DateTimeField(auto_now_add=True)

class authorities(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField(max_length=20)
    location = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

class NormalUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)