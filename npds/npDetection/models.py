from django.db import models

# Create your models here.
class numberplate(models.Model):
    numberPlate = models.CharField(max_length=20)
    colour = models.CharField(max_length=10)
    picture = models.CharField(max_length=20)
    auth = models.IntegerField()
    dateAndTime = models.DateTimeField(auto_now_add=True)

