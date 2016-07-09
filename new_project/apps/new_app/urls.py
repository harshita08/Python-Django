from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout_view),
    url(r'^friend/(?P<id>\d+)$', views.add_friend),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^remove/(?P<id>\d+)$', views.remove),
]