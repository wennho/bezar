from django.conf.urls import patterns, url

from ads import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(r'^craigs/$', views.CraigsView.as_view(), name='craigs'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.UpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.DeleteView.as_view(), name='delete'),
)
