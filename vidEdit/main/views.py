from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Service, Portfolio


class ServicesPage(ListView):
    model = Service
    template_name = 'main/services.html'


class OnlyService(DetailView):
    model = Service
    template_name = 'main/service.html'


class PortfolioList(ListView):
    model = Portfolio
    template_name = 'main/portfolio.html'


# def index(request):
#     return render(request, 'main/index.html')


def index(request):
    services = Service.objects.all()
    portfolio = Portfolio.objects.all()

    response_data = {
        'services': services,
        'portfolio': portfolio,
    }

    return render(request, 'main/index.html', response_data)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


