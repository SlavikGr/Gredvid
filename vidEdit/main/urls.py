from django.urls import path
from . import views
from .views import ServicesPage, OnlyService

urlpatterns = [
    path('', views.index, name='home'),
    path('services', ServicesPage.as_view(), name='services'),
    path('services/<int:pk>/', OnlyService.as_view(), name='service')
]
