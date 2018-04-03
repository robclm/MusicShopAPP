from django.db import models
# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    country = models.CharField(max_length=100)

class Recording(models.Model):
    title = models.CharField(max_length=150)
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
    duration = models.CharField(max_length=150)

class Release(models.Model):
    title = models.CharField(max_length=150)
    artist = models.ForeignKey('Artist' , on_delete=models.SET_NULL , null=True)
    date= models.DateField()