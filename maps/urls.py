from django.urls import path
from . import views
from allauth.account.views import LoginView
from .views import auth_success, remove_favorite, get_filtered_locations

urlpatterns = [
    path("", views.homepage, name="home"),
    path('input_location/', views.input_location, name='input_location'),
    path('add_item/', views.add_item, name='add_item'),
    path('about/', views.about, name='about'),
    path('accounts/login/', LoginView.as_view(), name='account_login'),
    path('accounts/login_success/', auth_success,
         {'action': 'login'}, name='login_success'),
    path('accounts/logout_success/', auth_success,
         {'action': 'logout'}, name='logout_success'),
    path('account/signup/', views.register, name='signup'),
    path('account/my_account/', views.my_account, name='my_account'),
    path('edit_location/<int:location_id>/',
         views.edit_location, name='edit_location'),
    path('delete_location/<int:location_id>/',
         views.delete_location, name='delete_location'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('location-data/', views.location_data, name='location-data'),
    path('toggle-favorite/<int:location_id>',
         views.toggle_favorite, name='toggle-favorite'),
    path('remove-favorite/<int:location_id>/',
         remove_favorite, name='remove_favorite'),
    path('get_filtered_locations', get_filtered_locations,
         name='get_filtered_locations'),
]
