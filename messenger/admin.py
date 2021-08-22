from django.contrib import admin
from django.contrib.messages.api import add_message
from .models import SmsTemplate
# Register your models here.
admin.site.register(SmsTemplate)