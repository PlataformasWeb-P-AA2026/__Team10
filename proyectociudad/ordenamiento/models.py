from django.db import models

# Create your models here.
from django.db import models


class Parroquia(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return "%s - %s - %s" % (
            self.nombre,
            self.ubicacion,
            self.tipo
        )


class BarrioCiudadela(models.Model):
    nombre = models.CharField(max_length=100)
    numero_viviendas = models.IntegerField()
    numero_parques = models.IntegerField()
    numero_edificios_residenciales = models.IntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - viviendas: %d - parques: %d - edificios: %d" % (
            self.nombre,
            self.numero_viviendas,
            self.numero_parques,
            self.numero_edificios_residenciales
        )


class PresidenteBarrio(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=100)
    edad = models.IntegerField()
    profesion = models.CharField(max_length=100)
    barrio = models.ForeignKey(BarrioCiudadela, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s - %d - %s" % (
            self.cedula,
            self.nickname,
            self.edad,
            self.profesion
        )
        
        
        
        