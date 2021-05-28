from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class User(AbstractUser):
    name = models.CharField(max_length=255, default="lim")
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


# Create your models here.
