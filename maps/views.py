from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LocationForm, ContactForm, RegistrationForm, LocationEditForm
from .models import Location, ContactMessage
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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


@login_required
def add_item(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            new_location = form.save(commit=False)
            new_location.user = request.user
            new_location.save()
            form.save_m2m()
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


# def location_list(request):
#     # Retrieve all Location objects from the database
#     locations = Location.objects.all()

#     # Pass the 'locations' queryset to the template
#     return render(request, 'index.html', {'locations': locations})


def location_data(request):
    locations = Location.objects.all().select_related('type').values(
        'latitude', 'longitude', 'notes', 'type', 'id'
    )
    location_list = list(locations)  # Convert QuerySet to list for JSON serialization
    return JsonResponse(location_list, safe=False)


def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(
                name=name, email=email, subject=subject, message=message)
            return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'about.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('login_success')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have logged in successfully.')
            return redirect('login_success')
        else:
            messages.error(
                request, 'Login was not successful. Please check your credentials.')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have logged out successfully.')
    return redirect('logout_success')


def auth_success(request, action):
    template = 'account/' + action + '_success.html'
    return render(request, template)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/signup.html', {'form': form})


@login_required
def my_account(request):
    user = request.user
    location_list = Location.objects.filter(user=user)
    paginator = Paginator(location_list, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'account/my_account.html', {'page_obj': page_obj})


def edit_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)

    if request.method == 'POST':
        form = LocationEditForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('my_account')
    else:
        form = LocationEditForm(instance=location)

    return render(request, 'edit_location.html', {'form': form, 'location': location})


def delete_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)

    if request.method == 'POST':
        location.delete()
        return redirect('my_account')

    return render(request, 'delete_location.html', {'location': location})


@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('home')
    else:
        return render(request, 'account/delete_account.html')

@csrf_exempt
def toggle_favorite(request, location_id):
    if request.method == 'POST':
        location = get_object_or_404(Location, id=location_id)
        user = request.user

        if user.is_authenticated:
            if user in location.favorited_by.all():
                location.favorited_by.remove(user)
            else:
                location.favorited_by.add(user)

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'User not authenticated'}, status=401)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)



