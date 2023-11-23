from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LocationForm, RegistrationForm, LocationEditForm
from .models import Location, ContactMessage, LocationType
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt


def homepage(request):
    """
    Render the homepage with a list of locations.
    """
    locations = Location.objects.all()
    types = LocationType.objects.values_list('name', flat=True).distinct()
    return render(request, 'index.html', {'locations': locations,
                                          'types': types})


def input_location(request):
    """
    Handle input for new location coordinates.

    Will automatically pull location data to for the add_item.html page.
    """
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
    else:
        form = LocationForm()

    return render(request, 'input_location.html', {'form': form})


@login_required
def add_item(request):
    """
    Handle the addition of a new location item.

    This view requires the user to be logged in.
    If not, user is redirected to the login page.
    """
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


def location_data(request):
    """
    Return a JSON response with location data.

    Fetches all locations and returns them in a JSON format.
    """
    locations = Location.objects.all().select_related('type').values(
        'latitude', 'longitude', 'notes', 'type', 'id'
    )
    location_list = list(locations)
    return JsonResponse(location_list, safe=False)


def about(request):
    """
    Render the 'about' page.
    """
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
    """
    Handles user login.
    """
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
    """
    Handle user login with additional messaging.

    Similar to the 'login' view but adds success or error messages.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have logged in successfully.')
            return redirect('login_success')
        else:
            messages.error(request,
                           'Login was not successful. Please check your credentials.')
    return render(request, 'login.html')


def logout_view(request):
    """
    Handle user logout.

    Logs out the user and redirects to a success page.
    """
    logout(request)
    messages.success(request, 'You have logged out successfully.')
    return redirect('logout_success')


def auth_success(request, action):
    """
    Display a success page for authentication actions.
    """
    template = 'account/' + action + '_success.html'
    return render(request, template)


def register(request):
    """
    Handle user registration with a custom form.
    """
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
    """
    Display the user's account page with their locations and favorites.

    This view requires the user to be logged in. Displays a paginated list of
    locations associated with the user and their favorite locations.
    """
    user = request.user
    location_list = Location.objects.filter(user=user)
    favorite_locations = user.favorite_locations.all()
    paginator = Paginator(location_list, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'favorite_locations': favorite_locations,
    }
    return render(request, 'account/my_account.html', context)


def edit_location(request, location_id):
    """
    Handle editing of a specific location.
    """
    location = get_object_or_404(Location, id=location_id)

    # Check if the logged-in user is the one who created the location
    if location.user != request.user:
        return render(request, 'forbidden.html', status=403)

    if request.method == 'POST':
        form = LocationEditForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            return redirect('my_account')
    else:
        form = LocationEditForm(instance=location)

    return render(request, 'edit_location.html', {'form':
                                                  form, 'location': location})


@login_required
@login_required
def delete_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)

    if location.user != request.user:
        return render(request, 'forbidden.html', status=403)

    if request.method == 'POST':
        location.delete()
        return redirect('success')

    return render(request, 'delete_location.html', {'location': location})


@login_required
def delete_account(request):
    """
    Handle the deletion of the user's account.
    """
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        return redirect('account_deletion')
    else:
        return render(request, 'account/delete_account.html')


@csrf_exempt
def toggle_favorite(request, location_id):
    """
    Handles users toggling favorite items.
    """
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
            return JsonResponse({'status': 'error', 'message':
                                 'User not authenticated'}, status=401)
    else:
        return JsonResponse({'status': 'error', 'message':
                             'Invalid request'}, status=400)


@login_required
def remove_favorite(request, location_id):
    """
    Handles users removing favorite items from account page.
    """
    if request.method == 'POST':
        location = Location.objects.get(id=location_id)
        request.user.favorite_locations.remove(location)
    return redirect('my_account')


def get_filtered_locations(request):
    """
    Handles users attempting to filter to a certain location type.
    """
    type_name = request.GET.get('type')
    if type_name:
        locations = Location.objects.filter(type__name=type_name).values(
            'latitude', 'longitude', 'type__name', 'notes', 'id')
    else:
        locations = Location.objects.all().values(
            'latitude', 'longitude', 'type__name', 'notes', 'id')

    return JsonResponse(list(locations), safe=False)


def success(request):
    return render(request, 'success.html')


def account_deletion(request):
    return render(request, 'account_deletion.html')
