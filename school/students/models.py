from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    standard = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='students/', null=True, blank=True)
    
    def __str__(self):
        return (f"{self.name} - {self.standard}")
