from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.principal, name='principal'),
	url(r'^academicos/nuevo/$', views.nuevo_academico, name='nuevo_academico'),
]
