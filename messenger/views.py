import django
from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from .models import SmsTemplate
from .forms import SmsTemplateForm
from django.contrib import messages

# Create your views here.
def sendSms(request):
    return render(request, 'messenger/send-sms.html', {})

def allSmsTemplates(request):
    if request.method == 'GET':
        templates = SmsTemplate.objects.order_by('id').reverse()
        return render(request, 'messenger/all-sms-templates.html', {'templates': templates})
    

def addSmsTemplate(request):
    form = SmsTemplateForm()
    if request.method == 'GET':
        return render(request, 'messenger/add-sms-template.html', {'form': form})
    if request.method == 'POST':
        form = SmsTemplateForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                templates = SmsTemplate.objects.order_by('id').reverse()
                messages.add_message(request, messages.SUCCESS, 'Template Added Successfully!')
                return render(request, 'messenger/all-sms-templates.html', {'templates': templates})
            else:
                messages.add_message(request, messages.ERROR, 'Please submit valid data!')
                return render(request, 'messenger/add-sms-template.html', {'form': form})
        except Exception as e:
            messages.add_message(request, messages.ERROR, e)
            return render(request, 'messenger/add-sms-template.html', {'form': form})


def editSmsTemplate(request, template_pk):
    template = get_object_or_404(SmsTemplate, pk=template_pk)
    form = None

    if request.method == 'GET':
        editSmsTemplateForm = SmsTemplateForm(instance=template)
        return render(request, 'messenger/edit-sms-template.html', {'form': editSmsTemplateForm, 'template': template})
    elif 'update' in request.POST:
        form = SmsTemplateForm(request.POST, instance=template)
        try:
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Template updated successfully!')
                return render(request, 'messenger/edit-sms-template.html', {'template': template, 'form': form})
        except ValueError:
            messages.add_message(request, messages.ERROR, 'Please submit valid data!')
            return render(request, 'messenger/edit-sms-template.html', {'template': template, 'form':form})
    elif 'delete' in request.POST:
        try:
            template.delete()
            messages.add_message(request, messages.SUCCESS, 'Template Deleted!')
            return redirect('allSmsTemplates')
        except Exception as e:
            messages.add_message(request, messages.ERROR, 'Something went wrong!')
            return render(request, 'messenger/edit-sms-template.html', {'template': template, 'form':form})