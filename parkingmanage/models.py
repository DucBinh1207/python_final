import code
from django.db import models

# Create your models here.
class ParkingLog(models.Model):
    logId = models.TextField(max_length=10)
    timeIn = models.DateTimeField()
    timeOut = models.DateTimeField()

class Vehicle(models.Model):
    licensePlate = models.TextField(max_length=10)
    type = models.TextField(max_length=255)
    brand = models.TextField(max_length=255)
    log = models.ForeignKey(ParkingLog, 
                            on_delete=models.CASCADE,
                            blank=False,
                            null=True)

class User(models.Model):
    code = models.TextField(max_length=10)
    email = models.EmailField()
    phone = models.TextField(max_length=255)
    address = models.TextField(max_length=255)
    vehicle = models.ForeignKey(Vehicle, 
                                on_delete=models.CASCADE,
                                blank=False,
                                null=True)

class Manager(models.Model):
    code = models.TextField(max_length=10)
    username = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
    role = models.TextField(max_length=255) #administrator quanly
    email = models.EmailField()
    phone = models.TextField(max_length=255)
