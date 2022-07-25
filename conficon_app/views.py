from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,  get_object_or_404, redirect
from django.views import generic
from .models import Profile, Icon, Result
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from conficon_app import SignUpForm #to be created in forms
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            login(request, user)
            messages.success(request, "Your registration was successful!")
            return redirect('home')
    
    else:
        form = SignUpForm()
    return render(request=request, template_name="signup.html", context={'signup_form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username, email or password.")
        else:
            messages.error(request, "Invalid details provided!")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})

def logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out of your account.")
    return redirect('home')

class IconList(generic.ListView):
    queryset = Icon.objects.all()
    template_name = 'index.html'

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

def upload(request):
    pass

def result(request):
    pass

