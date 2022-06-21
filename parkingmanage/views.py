from django.shortcuts import get_object_or_404, redirect, render
from parkingmanage.forms import LogForm, UserForm, VehicleForm
from parkingmanage.models import ParkingLog, User, Vehicle


# User View
def create_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()
        context = {'form': form, "alert_flag" : True}
    else : 
        context = {'form': form, "alert_flag" : False}
    return render(request, 'create.html', context)


def update_view(request, id):
    user = get_object_or_404(User, id=id)
    form = UserForm(request.POST or None, instance=user )
    if form.is_valid():
        form.save()
        return redirect('/parkingmanage')
    context = {'form': form}
    return render(request, 'create.html', context)


def delete_view(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('/parkingmanage')
    context = {'user': user}
    return render(request, 'delete.html', context)

def detail_view(request, id):
    user = get_object_or_404(User, id=id)
    vehicles = Vehicle.objects.all()
    context = {'user': user,'vehicles' : vehicles}
    return render(request, 'detail.html', context)

def list_view(request):
    keyword = request.GET.get('keyword')
    Selectsort = request.GET.get('selectsort')
    if Selectsort not in ['code', 'name', 'phone', 'email', 'address']:
        Selectsort = 'code'
    if keyword :
        users = User.objects.filter(code__icontains=keyword) | User.objects.filter(name__icontains=keyword) 
    else :
        users = User.objects.all()

    vehicles = Vehicle.objects.all()
    context = {
        'keyword': keyword,
        'users' :users.order_by(Selectsort),
        'vehicles' : vehicles
        }
    return render(request,"list.html",context)   
    
def view_vehicle(request, id):
    vehicles = Vehicle.objects.all()

    _delete = []
    for _vehicle in vehicles :
        if _vehicle.user.id == id :
            _delete.append(_vehicle.licensePlate)
    _vehicles = vehicles.filter(licensePlate__in=_delete)

    if (_vehicles.count() == 0):
        context = {'vehicles': _vehicles, "alert_flag" : True}
        return render(request, 'vehicleview.html', context)
    else : 
        context = {'vehicles': _vehicles, "alert_flag" : False}
        return render(request, 'vehicleview.html', context)
    
    
    context = {'vehicles': _vehicles}
    return render(request, 'vehicleview.html', context)

# Vehicle

def create_view_vehicle(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VehicleForm()
    context = {'form': form}
    return render(request, 'vehiclecreate.html', context)

def update_view_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    form = VehicleForm(request.POST or None, instance = vehicle )
    if form.is_valid():
        form.save()
        return redirect('/parkingmanage/vehicle')
    context = {'form': form}
    return render(request, 'vehiclecreate.html', context)

def detail_view_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    context = {'vehicle': vehicle}
    return render(request, 'vehicledetail.html', context)

def delete_view_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('/parkingmanage/vehicle')
    context = {'vehicle': vehicle}
    return render(request, 'vehicledelete.html', context)

def list_view_vehicle(request):
    keyword = request.GET.get('keyword')
    Selectsort = request.GET.get('selectsort')
    if Selectsort not in ['licensePlate','color' , 'type', 'brand']:
        Selectsort = 'licensePlate'
    if keyword :
        vehicles = Vehicle.objects.filter(licensePlate__icontains=keyword)| Vehicle.objects.filter(color__icontains=keyword ) | Vehicle.objects.filter(type__icontains=keyword ) | Vehicle.objects.filter(brand__icontains=keyword)
    else :
        vehicles = Vehicle.objects.all()
    context = {
        'keyword': keyword,
        'vehicles' :vehicles.order_by(Selectsort)    
        }
    return render(request,"vehiclelist.html",context)   

def view_log(request, id):
    logs = ParkingLog.objects.all()

    _delete = []
    for _log in logs :
        if _log.vehicle.id == id :
            _delete.append(_log.logId)
    _logs = logs.filter(logId__in=_delete)
    if (_logs.count() == 0):

        context = {'logs': _logs, "alert_flag" : True}
        return render(request, 'logview.html', context)
    else : 
        context = {'logs': _logs,"alert_flag" : False}
        return render(request, 'logview.html', context)
    
    


# Log View

def create_view_log(request):
    form = LogForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LogForm()
    context = {'form': form}
    return render(request, 'logcreate.html', context)

def update_view_log(request, id):
    log = get_object_or_404(ParkingLog, id=id)
    form = LogForm(request.POST or None, instance = log )
    if form.is_valid():
        form.save()
        return redirect('/parkingmanage/parkinglog')
    context = {'form': form}
    return render(request, 'logupdate.html', context)

def delete_view_log(request, id):
    log = get_object_or_404(ParkingLog, id=id)
    if request.method == 'POST':
        log.delete()
        return redirect('/parkingmanage/parkinglog')
    context = {'log': log}
    return render(request, 'logdelete.html', context)

def list_view_log(request):
    keyword = request.GET.get('keyword')
    Selectsort = request.GET.get('selectsort')
    if Selectsort not in ['logId', 'vehicle']:
        Selectsort = 'logId'
    if keyword :
        logs = ParkingLog.objects.filter(logId__icontains=keyword) | ParkingLog.objects.filter(vehicle__icontains=keyword)
    else :
        logs = ParkingLog.objects.all()
    context = {
        'keyword': keyword,
        'logs' :logs.order_by(Selectsort)    
        }
    return render(request,"loglist.html",context)   

#Parking Manage
def parking_view(request):
    return render(request, 'parkingmanager.html')
