# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Asignatura(models.Model):
	nombre=models.CharField(max_length=200)
	codigo=models.CharField(max_length=20)

class Academico(models.Model):
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	rut=models.CharField(max_length=20)
	asignatura=models.ManyToManyField(Asignatura)

class Carga(models.Model):
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	rut=models.CharField(max_length=20)
	academico = models.ForeignKey(Academico, on_delete=models.CASCADE)