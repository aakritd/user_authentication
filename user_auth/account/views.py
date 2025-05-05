from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        print(1)
        if form.is_valid():
            print(2)
            form.save()
        print(3)
        return redirect('login')
    else:
        print(4)
        form = RegisterForm()
    
    print(5)
    return render(response, "registration/register.html", {"form":form})