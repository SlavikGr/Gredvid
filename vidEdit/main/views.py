from django.shortcuts import render
from django.views.generic import ListView
from .models import Service


class ServicesPage(ListView):
    model = Service
    template_name = 'main/services.html'


def index(request):
    return render(request, 'main/index.html')


