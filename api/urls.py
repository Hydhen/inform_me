from django.conf.urls import url

from . import views

app_name = 'api'

urlpatterns = [
    url(r'^$', views.Home, name='home'),
    url(r'^about$', views.About, name='about'),
    url(r'^rules$', views.Rules, name='rules'),
    url(r'^staff$', views.Staff, name='staff'),
    url(r'^project$', views.Project, name='project'),
    url(r'^project/([0-9]+)$', views.ProjectId, name='projectId'),
    url(r'^login$', views.Login, name='login'),
    url(r'^islogged$', views.IsLogged, name='isLogged'),
    url(r'^logout$', views.Logout, name='logout'),
    url(r'^present_project$', views.PresentProject, name='present_project'),
    url(r'^contact$', views.Contact, name='contact')
]
