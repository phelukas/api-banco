from django.urls import path, re_path
from core import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    
    path("cliente/", views.ClienteView.as_view()),
    re_path("cliente/(?P<pk>\d+)", views.ClienteView.as_view()),
    path("banco/", views.BancoView.as_view()),
    re_path("banco/(?P<pk>\d+)", views.BancoView.as_view()),

    re_path("deposito/(?P<pk>\d+)", views.DepositoView.as_view()),
    re_path("saque/(?P<pk>\d+)", views.SaqueView.as_view()),
]
