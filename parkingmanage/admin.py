from django.contrib import admin
from .models import ParkingLog, Vehicle, User, Manager

# Register your models here.
admin.site.register(ParkingLog)
admin.site.register(Vehicle)
admin.site.register(User)
admin.site.register(Manager)
