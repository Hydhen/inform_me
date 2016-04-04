from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^about$', views.About, name='about'),
    url(r'^rules$', views.Rules, name='rules'),
    url(r'^staff$', views.Staff, name='staff'),
]
