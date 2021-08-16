from django.forms import ModelForm, widgets
from .models import Appointment
from django import forms

class AppointmentForm(ModelForm):
    # on_date = forms.DateField(widget=DatePicker())
    # at_time = forms.TimeField(
    #     widget=TimePicker(
    #         options={
    #             'enabledHours': [9, 10, 11, 12, 13, 14, 15, 16],
    #             'defaultDate': '1970-01-01T14:56:00'
    #         },
    #         attrs={
    #             'input_toggle': True,
    #             'input_group': False,
    #         },
    #     ),
    # )
    # note = forms.CharField(max_length=500)
    
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
            'on_date': widgets.DateInput(format='%d-%m-%Y', attrs={ 'type':'date', 'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),  
         }


