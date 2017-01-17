from django.shortcuts import render
from django.http import HttpResponse
from .models import Line
# Create your views here.

def home(request):
	#return HttpResponse("This is Soudeh reporting")
	#return render(request, "story/home.html", {'hello' : 'This page is just a test!'})
	return render(request, "story/home.html", {'lines' : Line.objects.all()})