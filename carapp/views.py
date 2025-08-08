from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def base(request):
    return render(request, 'base.html')

def Home(request):
    return render(request, 'home.html')

def Events_Hire(request):
    return render(request, 'Events_Hire.html')

def Car_Hire(request):
    return render(request, 'Car_Hire.html')

def Airport_transfer(request):
    return render(request, 'Airport_transfer.html')

def Booking(request):
    return render(request, 'Booking.html')

def Game_Drive(request):
    return render(request,'Game_Drive.html')

def Contacts(request):
    return render(request, 'contacts.html')

def Booking_success(request):
    return render(request, 'Booking_success.html')


def booking_view(request):
    if request.method == 'POST':
        service = request.POST.get('service')  # NEW FIELD
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        vehicle = request.POST.get('vehicle')
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')
        message = request.POST.get('message', '')

        subject = f'New {service} Booking from {name}'
        body = (
            f'Service Type: {service}\n'
            f'Name: {name}\n'
            f'Email: {email}\n'
            f'Phone: {phone}\n'
            f'Vehicle: {vehicle}\n'
            f'Pickup Date: {pickup_date}\n'
            f'Return Date: {return_date}\n'
            f'Message: {message}'
        )

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            ['maryokutse@gmail.com'],
            fail_silently=False,
        )

        return redirect('Booking_success')  

    return render(request, 'Booking.html')