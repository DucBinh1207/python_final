from django.urls import path
from .views import login_view, logout_view, create_view_log, create_view_vehicle, delete_view, delete_view_log, delete_view_vehicle, detail_view, create_view, detail_view_vehicle, list_view, list_view_log, list_view_vehicle, update_view, update_view_log, update_view_vehicle, view_log, view_vehicle, manage_view, create_view_manager, update_view_manager, delete_view_manager, detail_view_manager

urlpatterns = [
    path('login', login_view ,name ="login"),
    path('logout', logout_view ,name ="logout"),
    path('', list_view ,name ="list"),
    path('create', create_view, name='create'),
    path('<int:id>', detail_view, name='detail'),
    path('<int:id>/update', update_view, name='update'),
    path('<int:id>/delete', delete_view, name='delete'),
    path('<int:id>/viewvehicle', view_vehicle, name='view_vehicle'),
    path('vehicle', list_view_vehicle, name='list_vehicle'),
    path('vehicle/create', create_view_vehicle, name='create_vehicle'),
    path('vehicle/<int:id>', detail_view_vehicle, name='detail_vehicle'),
    path('vehicle/<int:id>/update', update_view_vehicle, name='update_vehicle'),
    path('vehicle/<int:id>/delete', delete_view_vehicle, name='delete_vehicle'),
    path('<int:id>/viewlog', view_log , name='view_log'),
    path('parkinglog', list_view_log, name='list_log'),
    path('parkinglog/create', create_view_log, name='create_log'),
    path('parkinglog/<int:id>/update', update_view_log, name='update_log'),
    path('parkinglog/<int:id>/delete', delete_view_log, name='delete_log'),
    path('manager', manage_view, name='manager'),
    path('manager/create', create_view_manager, name='create_manager'),
    path('manager/<int:id>/update', update_view_manager, name='update_manager'),
    path('manager/<int:id>/delete', delete_view_manager, name='delete_manager'),
    path('manager/<int:id>', detail_view_manager, name='detail_manager'),
]