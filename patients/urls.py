from django.urls import path
from . import views

urlpatterns = [
    path('addpatient/', views.addPatient, name='addPatient'),
    path('allpatients/', views.allPatients, name='allPatients'),
    path('editpatient/<int:patient_pk>', views.editPatient, name='editPatient'),
]