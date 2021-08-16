from appointments.models import Appointment
from appointments.forms import AppointmentForm
from django.shortcuts import render
from django.contrib import messages
from patients.models import Patient
from django.http import JsonResponse


# Create your views here.
def addAppointment(request):
    form = AppointmentForm()

    if request.method == 'GET':
        return render(request, 'appointments/add-appointment.html', {'form':form})
        
    elif request.method=='POST':
        form = AppointmentForm(request.POST) 
        try:
            patientName = request.POST['patient_name']
            date = request.POST['on_date']
            print(date)
            newApt = form.save(commit=False)
            patientName = request.POST['patient_name']
            patient = Patient.objects.get(patient_name=patientName)
            newApt.patient = patient  
            messages.add_message(request, messages.SUCCESS, 'Appointment Booked Successfully!')
            return render(request, 'appointments/add-appointment.html', {'form': AppointmentForm()})
        except Exception as e:
            messages.add_message(request, messages.ERROR, e)
            return render(request, 'appointments/add-appointment.html', {'form':form})
    return render(request, 'appointments/add-appointment.html', {})

def allAppointments(request):
    return render(request, 'appointments/all-appointments.html', {})

def fetchPatients(request):
    if 'term' in request.GET:
        patients = Patient.objects.filter(full_name__icontains=request.GET.get('term'))
        names = list()
        for patient in patients:
            names.append(patient.full_name)
        return JsonResponse(names, safe=False)
