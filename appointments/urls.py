from django.urls import path
from . views import *

urlpatterns = [
    path('addappointment/', addAppointment, name='addAppointment'),
    path('allappointments/', allAppointments, name='allAppointments'),
    path('fetchpatients', fetchPatients, name='fetchpatients'),

]