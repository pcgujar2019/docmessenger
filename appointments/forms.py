from django.forms import ModelForm, widgets
from .models import Appointment
from django import forms

class AppointmentForm(ModelForm):    
    class Meta:
        model = Appointment
        fields = '__all__'
        exclude = ['date_added', 'patient']
        labels = {
            'on_date': 'Date',
            'note': 'Note (optional)',
            'patient_name': 'Select Patient For Appointment',
        }
        widgets = { 
            'on_date': widgets.DateInput(format='%m-%d-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'mm-dd-yyyy'}),  
            'patient_name': widgets.TextInput(attrs={'autocomplete': 'off'})
         }


