# Create your views here.
from django.views.generic.simple import direct_to_template
from the_project.UserProfile.forms import RegistrationForm, UserProfileForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from the_project.UserProfile.models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            form.save_m2m()
            user.userprofile_set.create()
            return redirect('/')
    else:
        form = RegistrationForm()
    return direct_to_template(request=request, template='register.html', extra_context=locals())

def account(request):
    if request.user.is_authenticated():
        profile = request.user.get_profile()
        if request.method == 'POST':
            form = UserProfileForm(request.POST or None)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                return redirect('/account/')
        else:
            form = UserProfileForm(instance=profile)
        return direct_to_template(request=request, template='account.html', extra_context=locals())
    else:
        return redirect('/account/register/')
        
    
    