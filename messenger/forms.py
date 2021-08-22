from django.forms import ModelForm, widgets
from .models import SmsTemplate
from django import forms

class SmsTemplateForm(ModelForm):
    class Meta:
        model = SmsTemplate
        fields = '__all__'
        exclude = ['date_added']
        labels = {
            'sms_body': 'SMS Text',
        }
        widgets = { 
         }


