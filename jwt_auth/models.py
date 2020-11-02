from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    email = models.EmailField(unique=True)
    image = models.CharField(blank=True, max_length=200)
