from django.conf.urls import patterns, url
from server.views import GetTreeNode, Login, GetCards, GetRefuelingDetails, GetRootTable, GetTankDetails


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

str = '^(?P<username>\w+)/(?P<password>\w*)/(?P<fromDate>\d+\.\d+)/(?P<toDate>\d+\.\d+)/(?P<isMetric>\d{1})/%s/%s$'

urlpatterns = patterns('server.views',
    url(str % ('treenode', '(?P<dbindx>\w+)/'), GetTreeNode.as_view(), name='get_treenode'),
    url(str % ('root_table', ''), GetRootTable.as_view(), name='get_root_table'),
    url(str % ('refueling_details', '(?P<node>\w+)/'), GetRefuelingDetails.as_view(), name='get_refueling_details'),
    url(str % ('tank_details', '(?P<node>\w+)/'), GetTankDetails.as_view(), name='get_tank_details'),
    url(str % ('cards', '(?P<node>\w+)/'), GetCards.as_view(), name='get_cards'),
    url(r'^login/(?P<username>\w+)/(?P<password>\w*)/$', Login.as_view(), name='login')
    # url(r'^APIXServer/', include('APIXServer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
