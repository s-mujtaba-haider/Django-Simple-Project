from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    gender = models.BooleanField()
    address = models.TextField(max_length = 200)
    
class Car(models.Model):
    name = models.CharField(max_length = 500)
    speed = models.IntegerField(default = 100)