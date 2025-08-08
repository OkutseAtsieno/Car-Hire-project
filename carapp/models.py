from django.db import models

# Create your models here.

# carapp/models.py

from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    vehicle = models.CharField(max_length=50)
    pickup_date = models.DateField()
    return_date = models.DateField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.vehicle}'
