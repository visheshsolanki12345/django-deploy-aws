from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    roll = models.CharField(max_length=225, null=True, blank=True)
    city = models.CharField(max_length=225, null=True, blank=True)
    studentImage = models.ImageField(max_length=225, null=True, blank=True)