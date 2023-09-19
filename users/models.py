from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customers(AbstractUser):

    address = models.TextField()
    enterprise = models.CharField(max_length=70)