from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import LocationForm, ContactForm
from .models import Location, ContactMessage
# Create your views here.


def homepage(request):
    locations = Location.objects.all()

    return render(request, 'index.html', {'locations': locations})


def about(request):

    return render(request, 'about.html')


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


def location_list(request):
    # Retrieve all Location objects from the database
    locations = Location.objects.all()

    # Pass the 'locations' queryset to the template
    return render(request, 'index.html', {'locations': locations})


from django.shortcuts import render, redirect
from .forms import ContactForm

def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'about.html', {'form': form})

