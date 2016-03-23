#!/usr/bin/env python
import csv
import os
import sys
sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
from main.models import State, City
import django
django.setup()
# State.objects.all().delete()
dir_path = os.path.dirname(os.path.abspath(__file__))
states_csv = os.path.join(dir_path, 'city.csv')
csv_file = open(states_csv, 'r')
reader = csv.DictReader(csv_file)

for row in reader:
	try:
		state = State.objects.get(abbreviation=row['state'])
		new_city, created = City.objects.get_or_create(name=row['city'])
		new_city.state = state
		new_city.zip_code= row['zip_code']
		new_city.latitude = row['latitude']
		new_city.longitude = row['longitude']
		new_city.county = row['county']
		new_city.save()
	except Exception, e:
		print e
		print row


# print os.path.dirname(os.path.abspath(__file__)) + '/states.csv'
# print '%s/states.csv' % dir_path
# states = State.objects.all()
# for state in states:
# 	print state.name