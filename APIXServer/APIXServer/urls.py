from django.conf.urls import patterns, url
from server.views import GetCollection, Login


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('server.views',
    url(r'^get_collection/(?P<username>\w+)/(?P<password>\w*)/(?P<id>\w+)/$', GetCollection.as_view(), name='get_collection'),
    url(r'^login/(?P<username>\w+)/(?P<password>\w*)/$', Login.as_view(), name='login'),
    # url(r'^APIXServer/', include('APIXServer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
