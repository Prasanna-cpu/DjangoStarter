from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(default=18)
    email=models.EmailField()
    address=models.TextField()
    image=models.ImageField()
    file=models.FileField()
    field=models.DateTimeField(auto_now_add=True)