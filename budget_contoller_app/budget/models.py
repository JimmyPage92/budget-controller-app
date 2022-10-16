from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Income(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)