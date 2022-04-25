from django.shortcuts import render
from .models import ShippedProduct
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import YourMessageForm
from .models import YourMessage


def airfreight(request):
	return render(request, 'airfreight.html', {})


def oceanfreight(request):
	return render(request, 'oceanfreight.html', {})


def raillogistics(request):
	return render(request, 'raillogistics.html', {})


def roadlogistics(request):
	return render(request, 'roadlogistics.html', {})


def warehousing(request):
	return render(request, 'warehousing.html', {})

	
def index(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def fleet(request):
	return render(request, 'fleet.html', {})


def contact(request):
	if request.method == "POST":
		form = YourMessageForm(request.POST or None)
		if form.is_valid():
			name = request.POST.get('w3lName')
			email = request.POST.get('w3lSender')
			subject = request.POST.get('w3lSubect')
			message = request.POST.get('w3lMessage')
			new_message = YourMessage.objects.create(name=name, email=email, subject=subject, message=message)
			new_message.save()
			return HttpResponseRedirect(request.path_info) 
	else:
		form = YourMessageForm()
	return render(request, 'contact.html', {})


def service(request):
	return render(request, 'services.html', {})


def trackproduct(request):
	return render(request, 'trackproduct.html', {})


def covid(request):
	return render(request, 'covid.html', {})


def tracking(request):
	if request.method == 'GET':
		tracking = request.GET.get('tracking')
		products = ShippedProduct.objects.all().filter(tracking_id=tracking)
		
	return render(request, 'trackeddisplay.html', {"products": products, "tracking": tracking})

