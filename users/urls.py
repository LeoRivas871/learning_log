from django.urls import path, include

app_name = 'users'
urlpatterns = [
    #Incluye url de autenticación determinadas.
    path('',include('django.contrib.auth.urls')),
]