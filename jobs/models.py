from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length = 250)
    category = models.ForeignKey("Choice", on_delete=models.CASCADE)
    location = models.CharField(max_length = 250)
    company = models.CharField(max_length = 250)
    body = models.TextField()
    publish = models.DateTimeField()
    expire = models.DateTimeField()

    def __str__(self):
        return self.title 
    


class Choice(models.Model):
    category = models.CharField(max_length = 250)

    def __str__(self):
        return self.category
    