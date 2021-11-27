from django.db import models

# Create your models here.
class Register(models.Model):
    First_name = models.CharField(max_length=80)
    Last_name = models.CharField(max_length=80)
    Email = models.CharField(max_length=80)
    Phone_Number = models.IntegerField()
    Department = models.CharField(max_length=80)
    Level = models.IntegerField()