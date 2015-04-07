from django.conf.urls import patterns, url
from server.views import GetTreeNode, Login, GetCardDetails, GetCardSummary, GetRefuelingDetails, GetRootTable, GetTankDetails, GetTankWaterHeightDiagram, GetTankTemperatureDiagram, GetTankInventoryDiagram, GetControllerDetails, GetFuelGasDiagram, GetTankSummary, GetRefuelingSummary, GetControllerSummary, GetGroupDetails, GetGroupSummary

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

str = '^(?P<username>\w+)/(?P<password>\w*)/(?P<fromDate>\d+\.?\d+)/(?P<toDate>\d+\.?\d+)/%s/%s$'

urlpatterns = patterns('server.views',
    url(str % ('treenode', '(?P<dbindx>\w+)/(?P<treenodeType>\w+)/'), GetTreeNode.as_view(), name='get_treenode'),
    url(str % ('root_table', ''), GetRootTable.as_view(), name='get_root_table'),
    url(str % ('fuelgas_diagram', '(?P<controllerNum>\w+)/(?P<pistolNum>\w+)/(?P<language>\w+)/(?P<isMetric>\d{1})/'), GetFuelGasDiagram.as_view(), name='get_fuelgas_diagram'),
    url(str % ('refueling_details', '(?P<node>\w+)/(?P<treenodeType>\w+)/'), GetRefuelingDetails.as_view(), name='get_refueling_details'),
    url(str % ('refueling_summary', '(?P<node>\w+)/(?P<treenodeType>\w+)/'), GetRefuelingSummary.as_view(), name='get_refueling_summary'),

    url(str % ('tank_details', '(?P<node>\w+)/'), GetTankDetails.as_view(), name='get_tank_details'),
    url(str % ('tank_summary', '(?P<node>\w+)/'), GetTankSummary.as_view(), name='get_tank_summary'),

    url(str % ('tank_inventory_diagram', '(?P<tankNum>\w+)/(?P<language>\w+)/(?P<isMetric>\d{1})/'), GetTankInventoryDiagram.as_view(), name='get_tank_inventory_diagram'),
    url(str % ('tank_water_height_diagram', '(?P<tankNum>\w+)/(?P<language>\w+)/(?P<isMetric>\d{1})/'), GetTankWaterHeightDiagram.as_view(), name='get_tank_water_height_diagram'),
    url(str % ('tank_temperature_diagram', '(?P<tankNum>\w+)/(?P<language>\w+)/(?P<isMetric>\d{1})/'), GetTankTemperatureDiagram.as_view(), name='get_tank_temperature_diagram'),

    url(str % ('card_details', '(?P<node>\w+)/(?P<treenodeType>\w+)/'), GetCardDetails.as_view(), name='get_cards_details'),
    url(str % ('card_summary', '(?P<node>\w+)/(?P<treenodeType>\w+)/'), GetCardSummary.as_view(), name='get_cards_summary'),
    url(str % ('controller_details', '(?P<node>\w+)/'), GetControllerDetails.as_view(), name='get_controller_details'),
    url(str % ('controller_summary', '(?P<node>\w+)/'), GetControllerSummary.as_view(), name='get_controller_summary'),
    url(r'^login/(?P<username>\w+)/(?P<password>\w*)/$', Login.as_view(), name='login'),
    url(str % ('group_details', '(?P<node>\w+)/'), GetGroupDetails.as_view(), name='get_group_details'),
    url(str % ('group_summary', '(?P<node>\w+)/'), GetGroupSummary.as_view(), name='get_group_summary'),
    # url(r'^APIXServer/', include('APIXServer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
