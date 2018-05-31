from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return HttpResponse('<html><title>To-Do lists</title><body><h1>Hola Alex</h1></body></html>')