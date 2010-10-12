# Create your views here.
from django.views.generic.simple import direct_to_template
from the_project.UserProfile.forms import RegistrationForm, UserProfileForm,\
    SendMessageForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from the_project.UserProfile.models import UserProfile, Message

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
    return direct_to_template(request=request, template='registration/registration_form.html', extra_context=locals())

def account(request):
    user = request.user
    profile = user.get_profile()
    if user.is_authenticated():
        if request.method == 'POST':
            form = UserProfileForm(request.POST or None,instance=profile    )
            if form.is_valid():
                form.save()
                return redirect('/account/')
        else:
            form = UserProfileForm(instance=profile)
        a_projects = user.admin_project.all()
        m_projects = user.moder_project.all()
        num_messages = len(user.inbox.filter(is_new=True))
        return direct_to_template(request=request, template='account/account.html', extra_context=locals())
    else:
        return redirect('/account/register/')

def messages(request,type):
    user = request.user
    a_projects = user.admin_project.all()
    m_projects = user.moder_project.all()
    m_messages = []
    num_messages = len(user.inbox.filter(is_new=True))
    if type == 'inbox':
        m_messages = user.inbox.all()
    else:
        m_messages = user.outbox.all()
    return direct_to_template(request=request, template='account/inbox.html', extra_context=locals())

def detail_message(request,message_id):
    user = request.user
    m = get_object_or_404(Message,pk=message_id)
    num_messages = len(user.inbox.filter(is_new=True))
    m.is_new = False
    m.save()
    form = ''
    if m.to_user == user:
        form = SendMessageForm({'to_user':m.from_user})
    else:
        form = SendMessageForm({'to_user':m.to_user})
    a_projects = user.admin_project.all()
    m_projects = user.moder_project.all()
    return direct_to_template(request=request, template='account/detail_message.html', extra_context=locals())

def send_message(request):
    user = request.user
    if request.method == 'POST':
        username = request.POST['to_user']
        to_user = User.objects.get(username=username)
        subject = request.POST['subject']
        text = request.POST['text']
        if text and subject:
            m = Message(from_user = user, to_user=to_user, subject=subject,text=text)
            m.save()
    return redirect('/account/')