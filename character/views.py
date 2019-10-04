from django.shortcuts import render
from django.http import HttpResponse

def character(request):
   return render(request, 'character.html', {}) 
# Create your views here.
