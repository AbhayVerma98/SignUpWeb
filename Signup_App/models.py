from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12)


class User_details_Model(models.Model):
    CHOICE = (
        ('Patient', 'Patient'), ('Doctor', 'Doctor'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, default='a.jpg')
    user_type = models.CharField(choices=CHOICE, max_length=20,)
    state = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    pin_code = models.IntegerField(null=True)
    address = models.TextField(max_length=50)



