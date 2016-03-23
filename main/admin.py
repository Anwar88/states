from django.contrib import admin
from main.models import State, StateCapital, City
# Register your models here.


class StateCapitalAdmin(admin.ModelAdmin):
	list_display = ('name', 'longitude', 'latitude', 'capital_population')
	search_fields = ['name']

# class StateCapitalInline(admin.TabularInline):
# 	model = StateCapital

class StateAdmin(admin.ModelAdmin):
	list_display = ('name', 'abbreviation')
	search_fields =['name']
	# inlines = [StateCapitalInline]

class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'zip_code', 'latitude', 'longitude', 'county', 'state')
	search_fields = ['name']

admin.site.register(State, StateAdmin)
admin.site.register(StateCapital, StateCapitalAdmin)
admin.site.register(City, CityAdmin)


