from django.urls import path
from . import views  

urlpatterns = [
    path('', views.base, name='base'),
    path('Home', views.Home, name='home'),
    path('Events_Hire', views.Events_Hire, name='Events_Hire'),
    path('Car_Hire', views.Car_Hire, name='Car_Hire'),
    path('Airport_transfer', views.Airport_transfer, name='Airport_transfer'),

    
    path('Booking', views.booking_view, name='Booking'),

    path('Game_Drive', views.Game_Drive, name='Game_Drive'),
    path('Contacts', views.Contacts, name='Contacts'),
    path('Booking_success', views.Booking_success, name='Booking_success')
]
