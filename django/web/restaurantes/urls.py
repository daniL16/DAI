from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^$',views.restaurantes,name='restaurantes'),
  url(r'^registroRestaurante',views.restaurantes,name='registroRestaurante'),
  url(r'^editarRestaurante',views.restaurantes,name='editarRestaurante'),
  url(r'^registroUsuario',views.restaurantes,name='registroUsuario')
]