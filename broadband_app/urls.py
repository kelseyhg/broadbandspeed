from django.urls import path
from . import views
from djgeojson.views import GeoJSONLayerView

urlpatterns = [
    path('', views.info_scroll, name="main_page"),
    path('ajax/load-counties', views.load_counties, name="ajax_load_counties"),
  	path('ajax/chosen-county', views.chosen_county, name="chosen_county"),
]
