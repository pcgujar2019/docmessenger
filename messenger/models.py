from django.db import models

# Create your models here.
class SmsTemplate(models.Model):
    category = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=500)
    sms_body = models.TextField(max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)