from patients.models import Patient
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator

# Create your models here.

class PatientGender(models.TextChoices):
    MALE = 'Male' 
    FEMALE = 'Female'
class Appointment(models.Model):
    on_date = models.DateField(null=True)
    at_time = models.TimeField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    note = models.CharField(max_length=500, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient