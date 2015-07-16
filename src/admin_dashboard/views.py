from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'home.html', {})

def users(request):
	return render(request, 'users.html', {})

def pre_reg(request):
	return render(request, 'pre_reg.html', {})

def analytics(request):
	return render(request, 'analytics.html', {})