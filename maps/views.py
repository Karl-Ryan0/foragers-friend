from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import LocationForm
from .models import Location
# Create your views here.


def homepage(request):
    return render(request, "index.html")


def input_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            # Process or save the coordinates as needed
    else:
        form = LocationForm()

    return render(request, 'input_location.html', {'form': form})


def add_item(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']
            form.save()
            return redirect('/')
    else:
        form = LocationForm()

    return render(request, 'add_item.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def locationsList(request):
    data_from_database = YourModel.objects.all()
    return render(request, 'index.html', {'data_from_database': data_from_database})

