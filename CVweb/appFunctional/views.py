from django.shortcuts import render
from .models import *
from django.views.generic import DetailView

# Create your views here.
def Python(request):
    posts = modelPosteoPython.objects.all()
    context = {'posts':posts}
    return render (request, "Python.html", context)

def Html(request):
    posts = modelPosteoHTML.objects.all()
    context = {'posts': posts}
    return render(request, "HTML.html", context)

def Css(request):
    posts = modelPosteoCSS.objects.all()
    context = {'posts': posts}
    return render(request, "CSS.html", context)

class leerMasPython(DetailView):
    model = modelPosteoPython
    template_name = "leerMas.html"

class leerMasHtml(DetailView):
    model = modelPosteoHTML
    template_name = "leerMas.html"

class leerMasCss(DetailView):
    model = modelPosteoCSS
    template_name = "leerMas.html"
