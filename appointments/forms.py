from django.forms import ModelForm, widgets
from .models import Appointment

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        exclude = ['date_added']
        labels = {
            'on_date': 'Date',
            'at_time': 'Time',
            'patient': 'Select Patient For Appointment',
            'note': 'Note (optional)'
        }
        widgets = {
            'on_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'at_time': widgets.TimeInput(format='HH:MM', attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'HH:MM'}),
         }
