from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from main.models import State, StateCapital, City
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from main.forms import CitySearchForm, CreateCityForm, CityEditForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

# Create your views here.

def first_view(request, starts_with):
	text_string = ''

	states = State.objects.all()

	for state in states:
		cities = state.city_set.filter(name__startswith='%s' % starts_with)
		for city in cities:
			text_string += "State: %s, City: %s <br>" % (state, city.name)

	return HttpResponse(text_string)

def get_post(request):

	get_state = request.GET.get('state', None)
	get_city = request.GET.get('city', None)

	print get_state
	print get_city

	city_state_string = ""

	states = State.objects.filter(name__startswith="%s" % get_state)


	for state in states:
		cities = state.city_set.filter(name__startswith="%s" % get_city)

		for city in cities:
			city_state_string += "<b>%s</b> %s <br>" % (state, city.name)

	city_state_string += """
		<form action ="/get_post" method = "GET">

		State:
		<br>
		<input type="text" name="state">


		<br>


		City:
		<br>
		<input type = "text" name = "city">

		<br>
		<br>

		<input type ="submit" value="Submit">

		</form>
	"""

	response = city_state_string

	return HttpResponse(response)


# def template_view(request):

# 	context = {}

# 	states = State.objects.all()

# 	context ['states'] = states

# 	return render(request, 'state_list.html', context)


# def detail_view(request, pk):
	
# 	states = State.objects.get(pk=pk)

# 	context = {}

# 	context['states'] = states

# 	return render(request, 'detail_view.html', context)


# def list_view(request):
	
# 	states = State.objects.all()

# 	context = {}

# 	context = {'states'} = states

# 	return render(request, 'list_view.html', context)

def state_list(request):
	context ={}

	states = State.objects.all()

	context['states'] = states

	return render(request, 'state_list.html', context)

def state_detail(request, pk):

	context ={}

	states = State.objects.get(pk=pk)

	context['state'] = states

	return render(request, 'state_detail.html', context)

class StateListView(ListView):

	model = StateCapital

	template_name = 'state_list.html'

	context_object_name = 'states'


def city_search(request):
	request_context = RequestContext(request)

	context = {}

	if request.method == 'POST':
		form = CitySearchForm(request.POST)
		context['form'] = form 

		if form.is_valid():
			name = '%s' % form.cleaned_data['name']
			state = form.cleaned_data['state']

			context['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state) 


			return render_to_response('city_search.html', context, context_instance=request_context)

		else:
			context['valid'] = form.errors

			return render_to_response('city_search.html', context, context_instance=request_context)

	else: 
		form = CitySearchForm()
		context['form'] = form

		return render_to_response('city_search.html', context, context_instance=request_context)

@login_required
def city_create(request):
	request_context = RequestContext(request)

	context = {}

	if request.method == 'POST':
		form = CreateCityForm(request.POST)
		context['form']= form

		if form.is_valid():
			form.save()

			return render_to_response('city_create.html', context, context_instance=request_context)

		else:
				context['valid'] = form.errors
				return render_to_response('city_create.html', context, context_instance=request_context)
	else:
		form = CreateCityForm()
		context['form'] = form
		return render_to_response('city_create.html', context, context_instance=request_context)

@login_required
def city_edit(request, pk):
	request_context = RequestContext(request)

	context = {}

	city = City.objects.get(pk=pk)

	form = CityEditForm(request.POST or None, instance=city)

	context['form'] = form

	if form.is_valid():
		form.save()

		return redirect('/city_search/')

	return render_to_response('city_edit.html', context, context_instance=request_context)

@login_required
def city_delete(request, pk):

	City.objects.get(pk=pk).delete()

	return redirect('/city_search/')
		


