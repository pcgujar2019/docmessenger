
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patients/', include('patients.urls')),
    path('apt/', include('appointments.urls')),
    path('messenger/', include('messenger.urls')),
    path('', include('main.urls')),
]
