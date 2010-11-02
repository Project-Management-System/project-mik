# Create your views here.
from django.views.generic.simple import direct_to_template
from UserProfile.forms import RegistrationForm, UserProfileForm,\
    SendMessageForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from UserProfile.models import UserProfile, Message
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],form.cleaned_data['password'])
            user.save()
            user.userprofile_set.create()
            return redirect('/')
    else:
        form = RegistrationForm()
    return direct_to_template(request=request, template='registration/registration_form.html', extra_context=locals())

@login_required
def account(request):
    user = request.user
    profile = user.get_profile()
    if user.is_authenticated():
        if request.method == 'POST':
            form = UserProfileForm(request.POST or None,instance=profile)
            if form.is_valid():
                form.save()
                return redirect('/account/')
        else:
            form = UserProfileForm(instance=profile)
        profile = user.get_profile()
        return direct_to_template(request=request, template='account/account.html', extra_context=locals())
    else:
        return redirect('/account/register/')

@login_required
def messages(request,type):
    user = request.user
    a_projects = user.admin_project.all()
    m_projects = user.moder_project.all()
    if type == 'inbox':
        m_messages = user.inbox.all()
    else:
        m_messages = user.outbox.all()
    return direct_to_template(request=request, template='account/inbox.html', extra_context=locals())

@login_required
def detail_message(request,message_id):
    user = request.user
    m = get_object_or_404(Message,pk=message_id)
    m.is_new = False
    m.save()
    if m.to_user == user:
        form = SendMessageForm({'to_user':m.from_user})
    else:
        form = SendMessageForm({'to_user':m.to_user})
    profile = user.get_profile()
    return direct_to_template(request=request, template='account/detail_message.html', extra_context=locals())

@login_required
def send_message(request):
    user = request.user
    if request.method == 'POST':
        form = SendMessageForm(request.POST or None)
        to_user = request.POST['to_user']
        to_user = get_object_or_404(User,username=to_user)
        text = request.POST['text']
        if form.is_valid():
            m = Message(from_user = user, to_user=to_user, subject=form.cleaned_data['subject'],text=form.cleaned_data['text'])
            m.save()
            return redirect('/account/')
    else:
        form = SendMessageForm()
    return direct_to_template(request, 'account/detail_message.html', locals())