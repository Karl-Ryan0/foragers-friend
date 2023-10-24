from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path('input_location/', views.input_location, name='input_location'),
    path('add_item/', views.add_item_view, name='add_item'),
]
