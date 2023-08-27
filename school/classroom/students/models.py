from django.db import models

# Create your models here.
class Studentregister(models.Model):
    name = models.CharField(max_length=100)
    standard = models.CharField(max_length=20)
    phone = models.IntegerField()
