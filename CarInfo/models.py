from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User_type(models.Model):
    type=models.CharField(max_length=50)
class UserInfo(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mob = models.IntegerField()
    user_type = models.ForeignKey(User_type,on_delete=models.CASCADE)



class Company(models.Model):
    cname=models.CharField(max_length=20)
    clogo=models.ImageField()
    csite=models.CharField(max_length=50)


class CarInfo(models.Model):
    carname=models.CharField(max_length=50)
    carspec=models.CharField(max_length=50)
    blueprint=models.FileField()






