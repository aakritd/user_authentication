from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home(request):
    return render(request, 'account/home.html')

@login_required
def about(request):
    return render(request, 'account/about.html')

@login_required
def settings(request):
    return render(request, 'account/settings.html')

@login_required
def profile(request):
    return render(request, 'account/profile.html')

# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            # Save the User object
            new_user.save()
            return render(
               request,
               'registration/registration_done.html',
               {'new_user': new_user}
           )
    else:
        user_form = RegisterForm()
    return render(
        request,
        'registration/register.html',
        {'form': user_form}
    )