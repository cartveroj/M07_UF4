from django.db import models

# Create your models here.
class User(models.Model):
    rols =[
        ("student","student"),
        ("teacher","teacher")
    ]
    name = models.CharField(max_length = 100)
    first_last_name = models.CharField(max_length=50)
    second_last_name = models.CharField(max_length=50)
    rol = models.CharField(max_length=30, choices=rols)
    email = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    modules = models.CharField(max_length=30)