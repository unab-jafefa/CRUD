from django.urls import path
from . import views
from .views import agendaView ##Importo la clase que cree en views.py

urlpatterns = [
    path('', views.home),
    path('registrarCita/', views.registro),
    path('edicionAgenda/<id>', views.edicionAgenda),
    path('editarCita/', views.editarCita),
    path('eliminacionCitas/<id>', views.eliminar),
    path('agendas/', agendaView.as_view(), name='apis'), ##trato la clase como una vista
    path('agendas/<int:id>', agendaView.as_view(), name='apis_process') ##trato la clase como una vista
]