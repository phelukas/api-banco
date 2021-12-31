from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from django.urls import path, re_path
from core import views

urlpatterns = [

    path("user/", views.UserView.as_view()),
    
    path("cliente/", views.ClienteView.as_view()),
    re_path("cliente/(?P<pk>\d+)", views.ClienteView.as_view()),
    path("banco/", views.BancoView.as_view()),
    re_path("banco/(?P<pk>\d+)", views.BancoView.as_view()),

    re_path("deposito/(?P<pk>\d+)", views.DepositoView.as_view()),
    re_path("saque/(?P<pk>\d+)", views.SaqueView.as_view()),

    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),    
]
