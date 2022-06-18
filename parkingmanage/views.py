from django.shortcuts import get_object_or_404, redirect, render
from parkingmanage.forms import UserForm
from parkingmanage.models import ParkingLog, User, Vehicle, Manager

# Login Views
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            manage = get_object_or_404(Manager, username=username, password=password)
            if manage is not None:
                request.session['username'] = username
                return redirect('/parkingmanage')
        except:
            context = {
                'error': 'Username or Password is incorrect.',
                'display': 'block'
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html', { 'display': 'none'})

def login_validate(request, username, password):
    try:
        manage = get_object_or_404(Manager, username=username, password=password)
        if manage is not None:
            request.session['username'] = username
            return redirect('/parkingmanage')
    except:
        return render(request, 'login.html', {'error': 'Username or Password is incorrect.'})


# User View
def create_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()
    context = {'form': form}
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
    context = {'user': user}
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

# Vehicle View

def detail_view_vehicle(request, licensePlate):
    vehicle = get_object_or_404(Vehicle, licensePlate=licensePlate)
    context = {'vehicle': vehicle}
    return render(request, 'vehicledetail.html', context)

def list_view_vehicle(request):
    keyword = request.GET.get('keyword')
    Selectsort = request.GET.get('selectsort')
    if Selectsort not in ['licensePlate', 'type', 'brand']:
        Selectsort = 'licensePlate'
    if keyword :
        vehicles = Vehicle.objects.filter(code__icontains=keyword) | Vehicle.objects.filter(name__icontains=keyword) 
    else :
        vehicles = Vehicle.objects.all()
    context = {
        'keyword': keyword,
        'vehicles' :vehicles.order_by(Selectsort)    
        }
    return render(request,"vehiclelist.html",context)   

# Log View


def list_view_log(request):
    keyword = request.GET.get('keyword')
    Selectsort = request.GET.get('selectsort')
    if Selectsort not in ['logId', 'timeIn', 'timeOut']:
        Selectsort = 'logId'
    if keyword :
        logs = ParkingLog.objects.filter(code__icontains=keyword) | ParkingLog.objects.filter(name__icontains=keyword) 
    else :
        logs = ParkingLog.objects.all()
    context = {
        'keyword': keyword,
        'logs' :logs.order_by(Selectsort)    
        }
    return render(request,"loglist.html",context)   
