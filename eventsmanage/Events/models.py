from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.IntegerField(default=1)
    description = models.TextField(default='')
    location = models.CharField(max_length=255, default='')
    organizer = models.CharField(max_length=100, default='')


def __str__(self):
    return self.name
