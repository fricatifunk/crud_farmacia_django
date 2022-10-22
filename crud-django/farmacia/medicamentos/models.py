from django.db import models

# Create your models here.
class Remedio(models.Model):
    codigo=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    laboratorio=models.CharField(max_length=50)
    fechaIngreso=models.DateField()