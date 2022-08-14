import glob
import os
from zipfile import ZipFile

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files.images import ImageFile as File
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views import generic
from PIL import Image

from .models import Icon, Profile, Result


def index(request):
    if "my_sizes" in request.session:
        del request.session["my_sizes"]
    recent_fav = {}
    if request.user.is_authenticated:
        recent_fav = Result.objects.filter(user=request.user)
    return render(request, "index.html", {"icons": recent_fav})


"""@login_required(login_url="/login")
def authorized_page(request):
    return render(request, "authorized-page.html", {})
"""


def signup_view(request):
    if "my_sizes" in request.session:
        del request.session["my_sizes"]
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
        if password and username and email:
            try:
                Profile.objects.get(email=email)
            except:
                user = Profile(username=username.lower(), email=email)
                user.set_password(password)
                user.save()
                login(
                    request, user, backend="django.contrib.auth.backends.ModelBackend"
                )
                messages.success(request, "Your registration was successful!")
                return redirect("home")
            else:
                messages.error(request, "User exists, please login")
        else:
            messages.error(request, "Password, username or email cannot be empty")
    context = {"instance": instance}
    return render(request, "signup.html", context)


def contact(request):
    if "my_sizes" in request.session:
        del request.session["my_sizes"]
    if request.method == "POST":
        message = request.POST.get("message")
        email = request.POST.get("email")
        email = request.POST.get("email")
        message = request.POST.get("message")

        data = {
            "message": message,
            "email": email,
            "email": email,
            "message": message,
        }
        meaasge = """
        New message: {}

        From: {}
        """.format(
            data["message"], data["email"]
        )
        send_mail(data["email"], message, "", ["youngmaurizz@gmail.com"])
        return redirect("contact_sent")

    return render(request, "contact.html", {})


def contact_sent(request):
    if "my_sizes" in request.session:
        del request.session["my_sizes"]
    return render(request, "contact_sent.html")


def login_view(request):
    if "my_sizes" in request.session:
        del request.session["my_sizes"]
    """redirects to home is user is already logged in."""
    if request.user.is_authenticated:
        messages.info(
            request, "You are already authenticated! Log out to a create new account."
        )
        return redirect("home")
    if request.META["QUERY_STRING"].startswith("next="):
        messages.info(request, "You must login first to access that page")

    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")
        rememberbox = request.POST.get("rememberbox")
        if password and email:
            try:
                user = Profile.objects.get(email=email)
            except:
                messages.error(request, "User does not exists!")
            else:
                user = authenticate(username=email, password=password)
                if user:
                    login(
                        request,
                        user,
                        backend="django.contrib.auth.backends.ModelBackend",
                    )

                    # This is setting session to clear(when the browser was closed),
                    # if checkbox is not ticked else it will use the default
                    # session
                    if not rememberbox:
                        request.session.set_expiry(0)

                    messages.info(request, f"You are now logged in as {user.username}.")
                    return redirect("home")
                else:
                    messages.error(request, "Invalid password or email.")
        else:
            messages.error(request, "Password, or email cannot be empty")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out of your account.")
    return redirect("home")


@login_required(login_url="/login")
def upload(request):
    if "my_sizes" in request.session:
        del request.session["my_sizes"]
    if request.method == "POST":
        file_input = request.FILES["file-input"]

        icon = Icon.objects.create(
            name=str(file_input), user=request.user, image=file_input
        )
        print(icon, "myicon")
        return render(request, "index.html", {"icon": icon})
    else:
        return redirect("home")


def rm(name, sm=""):
    try:
        os.remove(name)
    except:
        pass


@login_required(login_url="/login")
def result(request):
    if request.method == "GET":
        return redirect("home")
    user_latest = Icon.objects.filter(user=request.user).first()
    name = "favicon%sx%s.ico"
    sizes = []
    post = request.POST
    for i in post:
        if i.startswith("s"):
            sizes.append((int(post[i]), int(post[i])))
    with (
        Image.open(user_latest.image.path) as img,
        ZipFile("media/favicon.zip", "w") as zip_obj,
    ):
        for size in sizes:
            img.save(name % size, sizes=(size,))
            zip_obj.write(name % size)
            rm(name % size)
        name = f"media/favicon{user_latest.id}.ico"
        img.save(name, sizes=sizes)
        zip_obj.write(name)
        fav = open(name, "rb")
        fav = Icon.objects.create(name=name, image=File(fav), user=request.user)
    zipf = open("media/favicon.zip", "rb")
    zipf = File(zipf)
    result = Result.objects.create(
        name=f"{user_latest.name}_{user_latest.id}",
        upload=fav,
        zip_file=zipf,
        user=request.user,
    )
    sizes = list(map(lambda x: f"{x[0]}x{x[0]}", sizes))
    request.session["my_sizes"] = " ".join(sizes)
    print(request.session["my_sizes"])
    return redirect("dashboard")


@login_required(login_url="/login")
def dashboard(request):
    latest_file = Result.objects.filter(user=request.user).first()
    recent_fav = Result.objects.filter(user=request.user)

    context = {"latest_icon": latest_file, "icons": recent_fav}
    return render(request, "dashboard.html", context)


def view_404(request, exception=None):
    return redirect("home")
