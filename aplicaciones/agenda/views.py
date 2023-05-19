from typing import Any
from django import http
from django.shortcuts import render,redirect
from django.http.response import JsonResponse ##importo la libreria que retorna un JSON
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Agenda
from django.views import View
import json

# Create your views here.

def home(request):
    agenda = Agenda.objects.all() ##accede al modelo y lo almacena en una variable
    return render(request, "gestionCitas.html", {"agenda": agenda} ) ## en el segundo parametro manda la variable como un objeto

def registro(request):
    id = request.POST['id']
    nombreCliente = request.POST['nombreCliente']
    nombreAbogado = request.POST['nombreAbogado']
    date = request.POST['date']

    agenda = Agenda.objects.create(id=id, nombreCliente=nombreCliente, nombreAbogado=nombreAbogado, date=date)
    return redirect('/')

def editarCita(request):
    id = request.POST['id']
    nombreCliente = request.POST['nombreCliente']
    nombreAbogado = request.POST['nombreAbogado']
    date = request.POST['date']


    agenda = Agenda.objects.get(id=id)
    agenda.nombreAbogado = nombreAbogado
    agenda.nombreCliente = nombreCliente
    agenda.date = date

    agenda.save()

    return redirect('/')

def edicionAgenda(request,id):
    agenda = Agenda.objects.get(id=id)
    return render(request, "edicionAgenda.html", {"agenda": agenda} )

def eliminar(request,id):
    agenda = Agenda.objects.get(id=id)
    agenda.delete()
    return redirect('/')

class agendaView(View):
        
        #reemplaza la validacion csrf
        @method_decorator(csrf_exempt)
        def dispatch(self, request, *args, **kwargs):
             return super().dispatch(request, *args, **kwargs)
        
        def get(self, request,id=0):
            if(id>0):
                agendas=list(Agenda.objects.filter(id=id).values())
                print(agendas)
                if len(agendas)>0:
                    agenda=agendas[0]
                    datos={'message':"success", 'agendas':agenda}
                else:
                    datos={'message':"agendas not found"}
                return JsonResponse(datos)
            else:
                agendas = list(Agenda.objects.values()) ##retorna los valores del modelo como un listado de objetos
                if len(agendas)>0:
                    datos={'message':"success", 'agendas':agendas}
                else:
                    datos={'message':"agendas not found"}
                return JsonResponse(datos)
        
        def put(self, request):
             pass
        
        def post(self, request):
             jd = json.loads(request.body)
             Agenda.objects.create(id=jd['id'], nombreCliente=jd['nombreCliente'], nombreAbogado=jd['nombreAbogado'], date=jd['date'])
             datos={'message':"success"}
             return JsonResponse(datos)
        
        def delete(self, request):
             pass

