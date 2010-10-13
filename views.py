# Create your views here.
from django.views.generic.simple import direct_to_template
from Projects.models import Project, News
from UserProfile.forms import LoginForm
from django.contrib.auth import get_user
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import Http404
from Projects.forms import AddNewsForm


def detail_user(request,user_id):
    user = get_object_or_404(User,pk=user_id)
    profile = user.get_profile()
    return direct_to_template(request=request, template='detail_user.html', extra_context={'u':user,
                                                                                           'profile':profile,
                                                                                           })
