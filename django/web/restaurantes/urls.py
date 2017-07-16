from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^$',views.restaurantes,name='restaurantes'),    
  url(r'^add/$', views.add, name='add'),
  url(r'^search/$', views.search, name='search'),
  url(r'^delete/$', views.delete, name='delete')
]