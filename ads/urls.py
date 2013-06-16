from django.conf.urls import patterns, url

from ads import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)