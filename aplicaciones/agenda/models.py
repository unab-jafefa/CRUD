
from django.db import models

# Create your models here.
class Agenda(models.Model):
        id = models.CharField(primary_key=True,max_length=6)
        nombreCliente = models.CharField(max_length=50)
        nombreAbogado = models.CharField(max_length=50)
        date = models.DateField()
        
        def __str__(self):
            texto = "id: {0} - Nombre Cliente: {1} - Nombre Abogado: {2} - Fecha Cita: {3}" ##concatena el texto
            return texto.format(self.id, self.nombreCliente, self.nombreAbogado, self.date) ##retorna los valores 
