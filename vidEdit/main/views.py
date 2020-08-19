from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Service, Portfolio


class ServicesPage(ListView):
    model = Service
    template_name = 'main/services.html'


class OnlyService(DetailView):
    model = Service
    template_name = 'main/service.html'


class Portfolio(ListView):
    model = Portfolio
    template_name = 'main/portfolio.html'


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


