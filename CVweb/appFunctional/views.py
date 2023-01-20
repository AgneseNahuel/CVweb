from django.shortcuts import render
from .models import *

# Create your views here.
def Python(request):
    posts = modelPosteo.objects.all()
    context = {'posts':posts}
    return render (request, "Python.html", context)