# import code
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    code = models.TextField(max_length=10)
    name = models.TextField(max_length=255, null=True)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')], null=True)
    email = models.EmailField(blank=False, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.name} "

    def get_absolute_url(self) : 
        return reverse('detail' ,kwargs = {"id" : self.id})

class Vehicle(models.Model):
    licensePlate = models.TextField(max_length=10)
    color = models.TextField(max_length=255, null=True)
    type = models.TextField(max_length=255, null=True)
    brand = models.TextField(max_length=255, null=True)
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            blank=True,
                            null=True)
    def __str__(self):
        return f"{self.licensePlate}"

    def get_absolute_url(self) : 
        return reverse('detail_vehicle' ,kwargs = {"id" : self.id})

class ParkingLog(models.Model):
    logId = models.TextField(max_length=10)
    timeIn = models.DateTimeField(null=True)
    timeOut = models.DateTimeField(null=True)
    vehicle = models.ForeignKey(Vehicle, 
                            on_delete=models.CASCADE,
                            blank=True,
                            null=True)    

    def __str__(self):
        return f"{self.logId}"


# class Manager(models.Model):
#     code = models.TextField(max_length=10)
#     username = models.TextField(max_length=255)
#     password = models.TextField(max_length=255)
#     role = models.TextField(max_length=255) #administrator quanly
#     phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
#     email = models.EmailField()
