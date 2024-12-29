'''Define patrones de url para learning_logs.'''
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Pagina de inicio
    path('',views.index,name='index'),
    #Página que muestra todos los temas.
    path('topics/', views.topics,name='topics'),
    #Página de detalles sobre un tema individual.
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    #Página para añadir un nuevo tema.
    path('new_topic/', views.new_topic, name='new_topic'),
    #Página para añadir una entrada nueva.
    path('new_entry/<int:topic_id>/',views.new_entry, name='new_entry')
]