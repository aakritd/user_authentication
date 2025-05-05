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