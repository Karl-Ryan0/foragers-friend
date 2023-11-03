from django.urls import path
from . import views
from allauth.account.views import LoginView
from .forms import CustomLoginForm

urlpatterns = [
    path("", views.homepage, name="home"),
    path('input_location/', views.input_location, name='input_location'),
    path('add_item/', views.add_item, name='add_item'),
    path('about/', views.about, name='about'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('account/login_success/', views.login_success, name='login_success'),
    path('account/logout_success/', views.logout_success, name='logout_success'),
    
]
