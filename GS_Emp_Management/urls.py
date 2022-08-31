from django.contrib import admin
from django.urls import path, include
from .views import home_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_index),
    path('employees/', include('employees.urls')),

]
