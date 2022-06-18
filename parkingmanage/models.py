# import code
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

# Create your models here.
class ParkingLog(models.Model):
    logId = models.TextField(max_length=10)
    timeIn = models.DateTimeField(null=True)
    timeOut = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.logId}"

class Vehicle(models.Model):
    licensePlate = models.TextField(max_length=10)
    type = models.TextField(max_length=255, null=True)
    brand = models.TextField(max_length=255, null=True)
    log = models.ForeignKey(ParkingLog, 
                            on_delete=models.CASCADE,
                            blank=True,
                            null=True)
    def __str__(self):
        return f"{self.licensePlate}"

    def getLog(self):
        return reverse('list_log')

class User(models.Model):
    code = models.TextField(max_length=10)
    name = models.TextField(max_length=255, null=True)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], null=True)
    email = models.EmailField(blank=False, null=True)
    address = models.TextField(blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, 
                                on_delete=models.CASCADE,
                                blank=False,
                                null=True)
    def __str__(self):
        return f"{self.code} - {self.name}"

    def get_absolute_url(self) : 
        return reverse('detail' ,kwargs = {"id" : self.id})

    def getVehicle(self) :
        return reverse('detail_vehicle' ,kwargs = {"licensePlate" : self.vehicle})

# class Manager(models.Model):
#     code = models.TextField(max_length=10)
#     username = models.TextField(max_length=255)
#     password = models.TextField(max_length=255)
#     role = models.TextField(max_length=255) #administrator quanly
#     phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
#     email = models.EmailField()
