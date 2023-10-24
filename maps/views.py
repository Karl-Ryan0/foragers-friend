from django.shortcuts import render
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
