from django.urls import path
from . import views

urlpatterns = [
    path('', views.sendSms, name='sendSms'),
    path('allsmstemplates/', views.allSmsTemplates, name='allSmsTemplates'),
    path('addsmstemplate/', views.addSmsTemplate, name='addSmsTemplate'),
    path('editsmstemplate/<int:template_pk>', views.editSmsTemplate, name='editSmsTemplate')
]