from . models import user
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return HttpResponse("<h1>This is home page</h1>")
def user(request):
    return render(request, 'login.html')

