from appointments.models import Appointment
from appointments.forms import AppointmentForm
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def addAppointment(request):
    form = AppointmentForm()

    if request.method == 'GET':
        return render(request, 'appointments/add-appointment.html', {'form':form})
        
    elif request.method=='POST':
        form = AppointmentForm(request.POST) 
        try:
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Appointment Booked Successfully!')
                return render(request, 'appointments/add-appointment.html', {'form': AppointmentForm()})
            else:
                messages.add_message(request, messages.ERROR, 'Please enter valid data!')
                return render (request, 'patients/add-appointment.html', {'form':AppointmentForm()})
        except ValueError:
            messages.add_message(request, messages.ERROR, 'Please submit valid data!')
            return render(request, 'main/add-appointment.html', {'form':form})
    return render(request, 'appointments/add-appointment.html', {})