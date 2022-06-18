from django.contrib import admin
from .models import ParkingLog, Vehicle, User

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('code','name','phone','email','address')
    list_filter = ('catogery',)

# Register your models here.
admin.site.register(ParkingLog)
admin.site.register(Vehicle)
admin.site.register(User)
# admin.site.register(Manager)
