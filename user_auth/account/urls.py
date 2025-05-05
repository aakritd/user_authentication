from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("password_change/", auth_views.PasswordChangeView.as_view(), name='password_change'),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # Password Reset when User forgets it
    path(
        'password-reset/', 
        auth_views.PasswordResetView.as_view(),
        name='password_reset'
    ),

    path(
        'password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),

    path(
        'password-reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),

    path(
        'password-reset/complete/', 
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),

    path('home/',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('settings/',views.settings, name='settings'),
    path('profile/',views.profile, name='profile'),
    path("register/", views.register, name="register")
    
]