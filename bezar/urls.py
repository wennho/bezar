from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bezar.views.home', name='home'),
    # url(r'^bezar/', include('bezar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^ads/', include('ads.urls', namespace="ads")),
    url(r'^accounts/', include('registration.backends.default.urls', namespace="accounts")),
    url(r'^admin/', include(admin.site.urls)),
)
