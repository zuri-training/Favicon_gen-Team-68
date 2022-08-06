from email import message
from socket import fromshare
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)