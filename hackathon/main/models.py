from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.


class User(AbstractUser):
   is_user = models.BooleanField(default=True)
   is_psychologist = models.BooleanField(default=False)

class Client(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

class Psychologist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    highest_qualifications = models.CharField(max_length=150)
    Clinic_location = models.TextField()
