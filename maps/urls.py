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
    path('account/signup/', views.register, name='signup'),
    path('account/my_account/', views.my_account, name='my_account'),
    path('edit_location/<int:location_id>/', views.edit_location, name='edit_location'),
    path('delete_location/<int:location_id>/', views.delete_location, name='delete_location'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
