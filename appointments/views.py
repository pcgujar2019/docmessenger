from time import time
from appointments.models import Appointment
from appointments.forms import AppointmentForm
from django.shortcuts import render
from django.contrib import messages
from patients.models import Patient
from django.http import JsonResponse
from datetime import date, datetime, timedelta


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
            newApt = form.save(commit=False)
            patientName = request.POST['patient_name']
            patient = Patient.objects.get(full_name=patientName)
            newApt.patient_name = patientName
            newApt.patient = patient  
            newApt.save()
            messages.add_message(request, messages.SUCCESS, 'Appointment Booked Successfully!')
            return render(request, 'appointments/add-appointment.html', {'form': AppointmentForm()})
        except Exception as e:
            messages.add_message(request, messages.ERROR, e)
            return render(request, 'appointments/add-appointment.html', {'form':form})

# This shows the today's, tomorrow's apoointments. Also datepicker to search appointment on a particular day
def allAppointments(request):
    todayDate = datetime.now()
    # Get today's appointments
    todayApts = Appointment.objects.filter(on_date=todayDate)
    #  Get tomorrow's appointments
    tomorrowApts = Appointment.objects.filter(on_date=(todayDate + timedelta(1)))
    if request.method == 'GET':
        return render(request, 'appointments/all-appointments.html', 
                {'todayApts': todayApts, 'tomorrowApts': tomorrowApts, 'today': todayDate, 'tomorrow': todayDate + timedelta(1)})

    elif 'searchByDate' in request.POST:
        date = request.POST['dateInput']
        aptsOnDate = Appointment.objects.filter(on_date=date)
        return render(request, 'appointments/all-appointments.html', 
                {'todayApts': todayApts, 
                'tomorrowApts': tomorrowApts, 
                'today': todayDate, 
                'tomorrow': todayDate + timedelta(1), 
                'aptsOnDate': aptsOnDate,
                'onDate': date})
        
def fetchPatients(request):
    if 'term' in request.GET:
        patients = Patient.objects.filter(full_name__icontains=request.GET.get('term'))
        names = list()
        for patient in patients:
            names.append(patient.full_name)
        return JsonResponse(names, safe=False)
