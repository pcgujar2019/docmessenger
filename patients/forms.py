from django.forms import ModelForm, widgets
from .models import Patient

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['date_added']
        labels = {
            'case_paper_number': 'Case Paper Number',
            'full_name': 'Full Name',
            'birth_date': 'Date of Birth',
            'mobile_number': 'Mobile Number',
            'pin_code': 'Pin Code',
            'referred_by': 'Referred By',
            'city': 'City/Town/Village'
        }
        widgets = {
            'case_paper_number': widgets.TextInput(attrs={'autocomplete': 'off'}),
            'full_name': widgets.TextInput(attrs={'autocomplete': 'off'}),
            'birth_date': widgets.DateInput(format= '%d-%m-%Y', attrs={'class':'form-control', 'autocomplete':'off', 'placeholder': 'dd-mm-yyyy'}),
            'mobile_number': widgets.NumberInput(attrs={'type': 'number'}),
            'email': widgets.EmailInput(),
            'pin_code': widgets.NumberInput(attrs={'required': 'required'}),
         }
