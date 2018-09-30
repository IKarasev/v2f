from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def mainpage(request):
	return render(request, 'general/mainpage.html')