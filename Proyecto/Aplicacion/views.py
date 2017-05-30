from __future__ import unicode_literals
from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

from .models import Academico
from django import forms


def principal(request):
	return render(request, 'Aplicacion/principal.html',{'var':Academico.objects.all()})

def nuevo_academico(request):
	if(request.method=='POST'):
		form=Form_nuevo_academico(request.POST)
		if form.is_valid():
			datos=form.cleaned_data
			nuevo=Academico()
			nuevo.rut=datos.get('rut')
			nuevo.nombre=datos.get('nombre')
			nuevo.apellido=datos.get('apellido')
			nuevo.save()
			return principal(request)
		else:
			return HttpResponse("datos invalidos");
		
	elif(request.method=='GET'):
		return render(request, 'Aplicacion/nuevo_academico.html')
	else:
		return HttpResponse('metodo no soportado')

class Form_nuevo_academico(forms.Form): #Note that it is not inheriting from forms.ModelForm
	nombre = forms.CharField(max_length=200)
	apellido = forms.CharField(max_length=200)
	#apellido = forms.CharField(max_length=200,required=False)
	rut = forms.CharField(max_length=20)