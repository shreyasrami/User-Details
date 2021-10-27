from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=50,unique=True)
    username = models.CharField(max_length=50,unique=True)
    address = models.CharField(max_length=200)

    USERNAME_FIELD  = 'email'

    REQUIRED_FIELDS = ['username']
