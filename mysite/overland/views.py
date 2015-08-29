from django.shortcuts import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.template import RequestContext

from .models import Application
from .models import ApplyForm
# Create your views here.

def index(request):
	return render(request, "overland/index.html")

def application(request):

	if request.method == 'GET':
		form = ApplyForm()
	else:
		form = ApplyForm(request.POST)
		if (form.is_valid()):
			try:
				subject = 'Overland Application'
				from_email = form.cleaned_data['useremail']
				phone = form.cleaned_data['phone']
				names = form.cleaned_data['names']
				year = form.cleaned_data['year']
				make = form.cleaned_data['make']
				model = form.cleaned_data['model']
				message = str(names) + '\n' + str(phone) + '\n' + str(year) + '\n' + str(make) + '\n' + str(model)
				try:
					send_mail(subject, message, from_email, ['rcd53@nau.edu'])
				except BadHeaderError:
					return HttpResponse('Invalid header found.')
				return redirect('thanks')
			except:
				pass
	return render(request, "overland/apply.html", {'form': form})

def route(request):
	return render(request, "overland/route.html")

def details(request):
	return render(request, "overland/details.html")

def participants(request):
	return render(request, "overland/participants.html")

def thanks(request):
	return render(request, "overland/thanks.html")

def gallery(request):
	return render(request, "overland/gallery.html")

def sponsors(request):
	return render(request, "overland/sponsors.html")