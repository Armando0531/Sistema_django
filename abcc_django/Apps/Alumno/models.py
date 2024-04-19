from django.db import models

# Create your models here.
class Alumno(models.Model):
    numcontrol = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    semestre = models.IntegerField()

    def __str__(self):
        texto = " {0} - {1} - {2}"
        return texto.format(self.numcontrol,self.nombre,self.semestre)