from django.urls import path
from .views import delete_view, detail_view, create_view, \
                    detail_view_vehicle, list_view, list_view_log, \
                    list_view_vehicle, update_view, login_view

urlpatterns = [
    path('login', login_view ,name ="login"),
    path('', list_view ,name ="list"),
    path('create', create_view, name='create'),
    path('<int:id>', detail_view, name='detail'),
    path('<int:id>/update', update_view, name='update'),
    path('<int:id>/delete', delete_view, name='delete'),
    path('vehicle', list_view_vehicle, name='list_vehicle'),
    path('vehicle/<str:licensePlate>', detail_view_vehicle, name='detail_vehicle'),
    path('log', list_view_log, name='list_log'),
]