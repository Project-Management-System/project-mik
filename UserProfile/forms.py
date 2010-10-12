from django import forms
from the_project.UserProfile.models import UserProfile, Message
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email')
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('is_banned','user')
        
class SendMessageForm(forms.Form):
    to_user = forms.CharField()
    subject = forms.CharField()
    text = forms.CharField(widget = forms.Textarea)