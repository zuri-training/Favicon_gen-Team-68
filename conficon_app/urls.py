from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup_view, name="signup"),
    path("upload/", views.upload, name="upload"),
    path("result/", views.result, name="result"),
    path("recent/", views.RecentIconList.as_view(), name="recent-icons"),
]
