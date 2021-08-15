from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator, MinValueValidator

# Create your models here.

class PatientGender(models.TextChoices):
    MALE = 'Male' 
    FEMALE = 'Female'
class Patient(models.Model):
    case_paper_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    age = models.IntegerField(blank=False, validators=[MinValueValidator(12), MaxValueValidator(65)])
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=PatientGender.choices, default=PatientGender.MALE)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    pin_code = models.IntegerField(blank=True, null=True)
    referred_by = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name