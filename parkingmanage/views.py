from django.shortcuts import get_object_or_404, redirect, render
from parkingmanage.forms import LogForm, UserForm, VehicleForm, ManagerForm
from parkingmanage.models import ParkingLog, User, Vehicle, Manager

# Login-Logout Views
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            manage = get_object_or_404(Manager, username=username, password=password)
            if manage is not None:
                request.session['username'] = username
                request.session['usertype'] = manage.role
                return redirect('/parkingmanage')
        except:
            context = {
                'error': 'Username or Password is incorrect.',
                'display': 'block'
            }
            return render(request, 'login.html', context)
    elif request.session['username'] is not None:
        return redirect('/parkingmanage')
    return render(request, 'login.html', { 'display': 'none' })

def logout_view(request):
    request.session['username'] = None
    request.session['usertype'] = None
    return render(request, 'login.html', { 'display': 'none' })

# User View
def create_view(request):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()
    context = {
        'mode': mode,
        'form': form
    }
    return render(request, 'create.html', context)


def update_view(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    user = get_object_or_404(User, id=id)
    form = UserForm(request.POST or None, instance=user )
    if form.is_valid():
        form.save()
        return redirect('/parkingmanage')
    context = {
        'mode': mode,
        'form': form
    }
    return render(request, 'create.html', context)

def delete_view(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('/parkingmanage')
    context = {
        'mode': mode,
        'user': user
    }
    return render(request, 'delete.html', context)

def detail_view(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    user = get_object_or_404(User, id=id)
    vehicles = Vehicle.objects.all()
    context = {
        'mode': mode,
        'user': user,
        'vehicles' : vehicles
    }
    return render(request, 'detail.html', context)

def list_view(request):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
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
        'mode': mode,
        'keyword': keyword,
        'users' :users.order_by(Selectsort),
        'vehicles' : vehicles
        }
    return render(request,"list.html",context)   
    
def view_vehicle(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    vehicles = Vehicle.objects.all()

    _delete = []
    for _vehicle in vehicles :
        if _vehicle.user.id == id :
            _delete.append(_vehicle.licensePlate)
    _vehicles = vehicles.filter(licensePlate__in=_delete)
    
    context = {
        'mode': mode,
        'vehicles': _vehicles
    }
    return render(request, 'vehicleview.html', context)

# Vehicle

def create_view_vehicle(request):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VehicleForm()
    context = {
        'mode': mode,
        'form': form
    }
    return render(request, 'vehiclecreate.html', context)

def update_view_vehicle(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    vehicle = get_object_or_404(Vehicle, id=id)
    form = VehicleForm(request.POST or None, instance = vehicle )
    if form.is_valid():
        form.save()
        return redirect('/parkingmanage/vehicle')
    context = {
        'mode': mode,
        'form': form
    }
    return render(request, 'vehiclecreate.html', context)

def detail_view_vehicle(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    vehicle = get_object_or_404(Vehicle, id=id)
    context = {
        'mode': mode,
        'vehicle': vehicle
    }
    return render(request, 'vehicledetail.html', context)

def delete_view_vehicle(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    vehicle = get_object_or_404(Vehicle, id=id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('/parkingmanage/vehicle')
    context = {
        'mode': mode,
        'vehicle': vehicle
    }
    return render(request, 'vehicledelete.html', context)

def list_view_vehicle(request):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    keyword = request.GET.get('keyword')
    Selectsort = request.GET.get('selectsort')
    if Selectsort not in ['licensePlate','color' , 'type', 'brand']:
        Selectsort = 'licensePlate'
    if keyword :
        vehicles = Vehicle.objects.filter(licensePlate__icontains=keyword)| Vehicle.objects.filter(color__icontains=keyword ) | Vehicle.objects.filter(type__icontains=keyword ) | Vehicle.objects.filter(brand__icontains=keyword)
    else :
        vehicles = Vehicle.objects.all()
    context = {
        'mode': mode,
        'keyword': keyword,
        'vehicles' :vehicles.order_by(Selectsort)    
        }
    return render(request,"vehiclelist.html",context)   

def view_log(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    logs = ParkingLog.objects.all()

    _delete = []
    for _log in logs :
        if _log.vehicle.id == id :
            _delete.append(_log.logId)
    _logs = logs.filter(logId__in=_delete)
    
    context = {
        'mode': mode,
        'logs': _logs
    }
    return render(request, 'logview.html', context)


# Log View

def create_view_log(request):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    form = LogForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LogForm()
    context = {
        'mode': mode,
        'form': form
    }
    return render(request, 'logcreate.html', context)

def update_view_log(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    log = get_object_or_404(ParkingLog, id=id)
    form = LogForm(request.POST or None, instance = log )
    if form.is_valid():
        form.save()
        return redirect('/parkingmanage/parkinglog')
    context = {
        'mode': mode,
        'form': form
    }
    return render(request, 'logupdate.html', context)

def delete_view_log(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    log = get_object_or_404(ParkingLog, id=id)
    if request.method == 'POST':
        log.delete()
        return redirect('/parkingmanage/parkinglog')
    context = {
        'mode': mode,
        'log': log
    }
    return render(request, 'logdelete.html', context)

def list_view_log(request):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    keyword = request.GET.get('keyword')
    Selectsort = request.GET.get('selectsort')
    if Selectsort not in ['logId', 'vehicle']:
        Selectsort = 'logId'
    if keyword :
        logs = ParkingLog.objects.filter(logId__icontains=keyword) | ParkingLog.objects.filter(vehicle__icontains=keyword)
    else :
        logs = ParkingLog.objects.all()
    context = {
        'mode': mode,
        'keyword': keyword,
        'logs' :logs.order_by(Selectsort)    
        }
    return render(request,"loglist.html",context)   

# Manage View
def manage_view(request):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    elif request.session['usertype'] == 'Staff':
        return redirect('/parkingmanage/')
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    
    managers = Manager.objects.all()
    context = {
        'usertype': usertype,
        'mode': mode,
        'managers': managers,
    }
    return render(request, 'managelist.html', context)

def create_view_manager(request):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    elif request.session['usertype'] == 'Staff':
        return redirect('/parkingmanage/')
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'

    form = ManagerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/parkingmanage/manager')
    context = {
        'mode': mode,
        'form': form
    }
    return render(request, 'managecreate.html', context)

def update_view_manager(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    elif request.session['usertype'] == 'Staff':
        return redirect('/parkingmanage/')
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'

    manager = get_object_or_404(Manager, id=id)
    form = ManagerForm(request.POST or None, instance = manager )
    if form.is_valid():
        form.save()
        return redirect('/parkingmanage/manager')
    context = {
        'mode': mode,
        'form': form
    }
    return render(request, 'manageupdate.html', context)

def delete_view_manager(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    elif request.session['usertype'] == 'Staff':
        return redirect('/parkingmanage/')
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'

    manager = get_object_or_404(Manager, id=id)
    if request.method == 'POST':
        manager.delete()
        return redirect('/parkingmanage/manager')
    context = {
        'mode': mode,
        'manager': manager,
    }
    return render(request, 'managedelete.html', context)

def detail_view_manager(request, id):
    mode = 'none'
    if request.session['username'] is None:
        return render(request, 'login.html', { 'display': 'none' })
    elif request.session['usertype'] == 'Staff':
        return redirect('/parkingmanage/')
    usertype = request.session['usertype']
    if usertype == 'Administrator' or usertype == 'Manager':
        mode = 'block'
    
    manager = get_object_or_404(Manager, id=id)
    context = {
        'mode': mode,
        'manager': manager,
    }
    return render(request, 'managedetail.html', context)