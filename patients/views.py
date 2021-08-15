from django.shortcuts import redirect, render, get_object_or_404
from .forms import PatientForm
from .models import Patient
from django.contrib import messages



def addPatient(request): 
    form = PatientForm()
    # Get last case paper number and set next to case paper number input 
    last_number = None
    casepapernumber = '1' 
    last_patient = Patient.objects.last()
    if last_patient:
        last_number = int(last_patient.case_paper_number)
        casepapernumber = last_number + 1

    if request.method == 'GET':
        return render(request, 'patients/add-patient.html', {'casepapernumber': casepapernumber, 'form':form})
        
    elif request.method=='POST':
        form = PatientForm(request.POST) 
        try:
            if form.is_valid():
                form.save()
                patients = Patient.objects.order_by('id').reverse()
                messages.add_message(request, messages.SUCCESS, 'Patient Added Successfully!')
                return render(request, 'patients/all-patients.html', {'patients': patients})
            else:
                return render (request, 'patients/add-patient.html', {'casepapernumber': casepapernumber, 'form':form})
        except ValueError:
            messages.add_message(request, messages.ERROR, 'Please submit valid data!')
            return render(request, 'main/add-patient.html', {'casepapernumber': casepapernumber, 'form':form})
    return render(request, 'patients/add-patient.html', {})

def allPatients(request):
    if request.method == 'GET':
        patients = Patient.objects.order_by('id').reverse()
        return render(request, 'patients/all-patients.html', {'patients': patients})


def editPatient(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    form = None
    if request.method == 'GET':
        editpatientform = PatientForm(instance=patient)
        return render(request, 'patients/edit-patient.html', {'patient': patient, 'form': editpatientform})
    elif 'update' in request.POST:
        form = PatientForm(request.POST, instance=patient)
        try:
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Patient updated successfully!')
                return render(request, 'patients/edit-patient.html', {'patient': patient, 'form': form})
        except ValueError:
            messages.add_message(request, messages.ERROR, 'Please submit valid data!')
            return render(request, 'patients/edit-patient.html', {'patient': patient, 'form':form})
    elif 'delete' in request.POST:
        try:
            patient.delete()
            messages.add_message(request, messages.SUCCESS, 'Patient Deleted!')
            return redirect('allPatients')
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong!')
            return render(request, 'patients/edit-patient.html', {'patient': patient, 'form':form})
