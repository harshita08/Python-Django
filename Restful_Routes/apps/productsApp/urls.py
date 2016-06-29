from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products$', views.index),
    url(r'^new$', views.new), 
    url(r'^create$', views.create),
    url(r'^products/show/(?P<id>\d+)$', views.show),
    url(r'^products/edit/(?P<id>\d+)$', views.edit),
    url(r'^products/update/(?P<id>\d+)$', views.update),
    url(r'^products/delete/(?P<id>\d+)$', views.destroy),
]
