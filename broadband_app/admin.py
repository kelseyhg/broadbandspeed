from django.contrib import admin

# Register your models here.
from .models import County, State

admin.site.register(County)
admin.site.register(State)