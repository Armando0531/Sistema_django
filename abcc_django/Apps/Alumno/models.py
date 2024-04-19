from django.db import models

# Create your models here.
class Alumno(models.Model):
    numcontrol = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    semestre = models.IntegerField()