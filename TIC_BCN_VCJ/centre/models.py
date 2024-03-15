from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 100)
    first_last_name = models.CharField(max_length=50)
    second_last_name = models.CharField(max_length=50)
    rol = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    modules = models.CharField(max_length=30)