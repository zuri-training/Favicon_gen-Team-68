from django import forms

from .models import Profile, Icon

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['email', 'username']

class IconForm(forms.ModelForm):

    class Meta:
        model = Icon
        fields = ['image']