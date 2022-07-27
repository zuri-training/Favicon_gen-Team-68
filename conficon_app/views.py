from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import redirect, render
from django.views import generic

from .models import Icon, Profile, Result


def index(request):
    return render(request, "index.html")


@login_required(login_url="/login")
def authorized_page(request):
    return render(request, "authorized-page.html", {})


def signup_view(request):
    """redirects to home is user is already logged in."""
    if request.user.is_authenticated:
        messages.info(
            request, "You are already authenticated! Log out to create new account."
        )
        return redirect("home")

    instance = {"username": "", "email": ""}
    if request.method == "POST":
        instance["username"] = username = request.POST.get("username")
        instance["email"] = email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            Profile.objects.get(email=email)
        except:
            user = Profile(username=username.lower(), email=email)
            user.set_password(password)
            user.save()
            login(request, user)
            messages.success(request, "Your registration was successful!")
            return redirect("home")
        else:
            messages.error(request, "User exists, please login")
    context = {"instance": instance}
    return render(request, "signup.html", context)


def login_view(request):
    """redirects to home is user is already logged in."""
    if request.user.is_authenticated:
        messages.info(
            request, "You are already authenticated! Log out to a create new account."
        )
        return redirect("authorized-page")
    if request.META["QUERY_STRING"].startswith("next="):
        messages.info(request, "You must login login first to access that page")

    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")
        rememberbox = request.POST.get("rememberbox")

        try:
            user = Profile.objects.get(email=email)
        except:
            messages.error(request, "User does not exists!")
        else:
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)

                # This is setting session to clear(when the browser was closed),
                # if checkbox is not ticked else it will use the default
                # session
                if not rememberbox:
                    request.session.set_expiry(0)

                messages.info(request, f"You are now logged in as {user.username}.")
                return redirect("home")
            else:
                # For security reasons, it's better to flash password or email
                messages.error(request, "Invalid password or email.")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out of your account.")
    return redirect("home")


class IconList(generic.ListView):
    queryset = Icon.objects.all()
    template_name = "index.html"

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)


def upload(request):
    pass


def result(request):
    pass
