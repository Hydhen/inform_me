from django.conf.urls import url

from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about$', views.about, name='about'),
    url(r'rules$', views.rules, name='rules'),
    url(r'staff$', views.staff, name='staff'),
]
