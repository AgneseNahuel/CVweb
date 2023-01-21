from django.shortcuts import render
from .models import *
from django.views.generic import DetailView

# Create your views here.
def Python(request):
    posts = modelPosteo.objects.all()
    context = {'posts':posts}
    return render (request, "Python.html", context)

class leerMas(DetailView):
    model = modelPosteo
    template_name = "leerMas.html"
