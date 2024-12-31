from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    #Incluye url de autenticación determinadas.
    path('',include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]