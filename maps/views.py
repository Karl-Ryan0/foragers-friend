from django.shortcuts import render, redirect
from .forms import LocationForm
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
            form.save()  # Save the item to the database
            return redirect('index.html')  # Redirect to a success page
    else:
        form = LocationForm()

    return render(request, 'add_item.html', {'form': form})
