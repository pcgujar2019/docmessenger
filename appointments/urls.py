from django.urls import path
from . views import *

urlpatterns = [
    path('addappointment/', addAppointment, name='addAppointment')
]