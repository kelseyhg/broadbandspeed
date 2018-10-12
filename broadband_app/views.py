from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import County, State
from django.urls import reverse_lazy
from .forms import LocationForm
from djgeojson.views import GeoJSONLayerView


# Create your views here.
def info_scroll(request):
	states = State.objects.all()
	form = LocationForm(auto_id=False)
	return render(request, 'info_scroll.html', {'form': form, 'states': states})


def load_counties(request):
	
	state_id = request.GET.get('state')
	print("state id", state_id)
	# counties = [("02", "my favorite county")]
	counties = County.objects.filter(state=state_id).order_by('name')
	print("counties", counties)
	# return httpResponse("HERE IS A RESPONSE") 
	return render(request, 'county_options.html', {'counties': counties })

def chosen_county(request):
	county_id = request.GET.get('county')
	county = County.objects.get(id=county_id)
	form = LocationForm(auto_id=False)
	states = State.objects.all()
	return render(request, 'chosen_county.html', {'county': county })
	#return HttpResponse('0.236754')

def us_map(request):
	return render(request, 'us_map.html')	

class MapLayer(GeoJSONLayerView):
	# Options
	precision = 4 # float
	simplify = 0.5 # generalization


