from django.db import models


# Create your models here.
class Message(models.Model):


    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    body = models.TextField()
