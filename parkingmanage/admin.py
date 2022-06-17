from django.contrib import admin
from .models import ParkingLog, Vehicle, User

class LoginLine(admin.StackedInline):
    model = ParkingLog

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('code','name','phone','email','address','catogery')
    list_filter = ('catogery',)
    inlines = [LoginLine]

# Register your models here.
admin.site.register(ParkingLog)
admin.site.register(Vehicle)
admin.site.register(User)
# admin.site.register(Manager)
