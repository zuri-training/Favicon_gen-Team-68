from django.urls import path
from django.contrib import admin

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("upload/", views.upload, name="upload"),
    path("result/", views.result, name="result"),

    #urls for password reset
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
    name="password_reset"), #goes to custom Django admin panel by default(override with template)

    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
    name="password_reset_confirm"),

    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
    name="password_reset_complete"),
]
