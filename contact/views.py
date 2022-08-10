from multiprocessing import context
from django.shortcuts import render
from .models import contactform

# Create your views here.

def contactus(request): 
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')

        contactformdata = contactform(email=email,message=message)
        contactformdata.save() 

    return render(request, 'contact.html')
