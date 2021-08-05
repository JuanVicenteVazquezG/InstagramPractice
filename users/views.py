"""User views."""
# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Exception
from django.db.utils import IntegrityError

@login_required
def update_profile(request):
    """Update a user's profile view"""
    return render(request,'users/update_profile.html')
    


def login_view(request):
    """Login views."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')


def signup_view(request):
    """Signup a user."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Error. Password confirmation does not match!'})
        try:
            user = User.objects.create_user(
                username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Error, this user {} already exist'.format(username)})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')
