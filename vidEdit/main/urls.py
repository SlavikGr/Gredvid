from django.urls import path
from . import views
from .views import ServicesPage

urlpatterns = [
    path('', views.index, name='home'),
    path('services', ServicesPage.as_view(), name='services')
]
