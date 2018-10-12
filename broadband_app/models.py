from django.db import models

# Create your models here.
class State(models.Model):
	name = models.CharField(max_length=100)
	state_id = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class County(models.Model):
	name = models.CharField(max_length=100)
	state = models.CharField(max_length=50)
	county_id = models.CharField(max_length=50) 
	median_speed = models.FloatField(max_length=20)

	def __str__(self):
		return self.name
