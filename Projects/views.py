from django.views.generic.simple import direct_to_template
from Projects.models import Project, News, Tag
from UserProfile.forms import LoginForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import Http404
from Projects.forms import AddNewsForm, AddProjectForm
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

def detail_project(request,project_id):
    News = get_object_or_404(Project,pk=project_id).news_set.order_by('-date')[:5]
    project = get_object_or_404(Project,pk=project_id)
    is_admin = project.is_admin(request.user)
    is_moder = project.is_moder(request.user)
    return direct_to_template(request, 'index.html', locals())

def detail_news(request,project_id,news_id):
    news = get_object_or_404(get_object_or_404(Project,pk=project_id).news_set,pk=news_id)
    project = get_object_or_404(Project,pk=project_id)
    is_admin = project.is_admin(request.user)
    is_moder = project.is_moder(request.user)
    return direct_to_template(request, 'detail_news.html', locals())

@login_required
def add_news(request,project_id):
    user=request.user
    project = get_object_or_404(Project,pk=project_id)
    if request.method == 'POST':
        form = AddNewsForm(request.POST or None)
        if project.is_moder(user):
            if form.is_valid():
                n=form.save(commit=False)
                n.user = user
                project.news_set.add(n)
                return redirect("/project/%d/" % (int(project_id)))
    else:
        form = AddNewsForm()
    is_admin = project.is_admin(user)
    is_moder = project.is_moder(user)
    return direct_to_template(request, 'add_news.html', locals())

@login_required
def delete_news(request,project_id,news_id):
    project = get_object_or_404(Project,pk=project_id)
    news = get_object_or_404(project.news_set,pk=news_id)
    is_moder = project.is_moder(request.user)
    if is_moder:
        news.delete()
        redirect('/project/%s/'%(project_id))
    return redirect('/project/%s/news/%s/'%(project_id,news_id))

@login_required
def edit_news(request,project_id,news_id):
    user=request.user
    project = get_object_or_404(Project,pk=project_id)
    news = get_object_or_404(project.news_set,pk=news_id)
    is_author = user == news.user
    if request.method == 'POST':
        if project.is_moder(user) or is_author:
            form = AddNewsForm(request.POST or None,instance = news)
            if form.is_valid():
                form.save()
                return redirect("/project/%s/news/%s/" % (project_id,news_id))
    else:
        form = AddNewsForm(instance = news)
    is_admin = project.is_admin(user)
    is_moder = project.is_moder(user)
    is_author = user == news.user
    return direct_to_template(request, 'add_news.html', locals())

@login_required
def new_project(request):
    user = request.user
    if request.method == 'POST':
        form = AddProjectForm(request.POST or None)
        if form.is_valid():
            tags = form.cleaned_data['_tags'].split()
            p = form.save()
            for i in tags:
                t = Tag.objects.get_or_create(text=i)[0]
                p.tags.add(t)
            p.admins.add(user)
            return redirect('/account/')
    else:
        form = AddProjectForm()
    return direct_to_template(request, 'add_project.html', locals())

def list_project_by_tag(request,tag):
    t = get_object_or_404(Tag,text=tag)
    projects = t.projects.all()
    return direct_to_template(request, 'list_projects.html', locals())

@login_required
def edit_project(request,project_id):
    user = request.user
    project = get_object_or_404(Project,pk=project_id)
    if request.method == 'POST':
        form = AddProjectForm(request.POST or None,instance=project)
        if form.is_valid() and project.is_admin(user):
            tags = form.cleaned_data['_tags'].split()
            form.save()
            project.tags.clear()
            for i in tags:
                t = Tag.objects.get_or_create(text=i)[0]
                project.tags.add(t)
            return redirect('/project/%s/'%(project_id))
    else:
        t = model_to_dict(project)
        t.update({'_tags':' '.join([i.text for i in project.tags.all()])})
        form = AddProjectForm(t)
    is_admin = project.is_admin(request.user)
    is_moder = project.is_moder(request.user)
    return direct_to_template(request, 'edit_project.html', locals())