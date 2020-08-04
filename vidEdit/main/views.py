from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Service


class ServicesPage(ListView):
    model = Service
    template_name = 'main/services.html'


class OnlyService(DetailView):
    model = Service
    template_name = 'main/service.html'


def index(request):
    return render(request, 'main/index.html')


