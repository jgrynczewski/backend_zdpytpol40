from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.age}) z {self.city}"

    def get_absolute_url(self):
        return reverse("view_examples:hello")
