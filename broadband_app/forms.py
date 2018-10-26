from django import forms
from .models import County, State

#states = [("01", "Delaware"), ("02", "New Jersey"), ("03", "Hawaii")]
states = State.objects.all()
statesTuples = [("null", "select state")]
for state in states:
	statesTuples.append((state.state_id, state.name))

counties = County.objects.all()
countiesTuples = [("null", "------------")]
for county in counties:
	countiesTuples.append((county.id, county.name))

#countiesTuples = [("02", "my favorite county")]

class LocationForm(forms.Form):
	state = forms.CharField(label="Pick a state", widget=forms.Select(choices=statesTuples, attrs={'class': 'state'}))
	county = forms.CharField(label="Pick a county", widget=forms.Select(choices=countiesTuples, attrs={'class': 'county'}))