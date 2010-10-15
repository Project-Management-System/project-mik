from django.views.generic.simple import direct_to_template
from Projects.models import Project, News, Tag
from UserProfile.forms import LoginForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import Http404
from Projects.forms import AddNewsForm, AddProjectForm
from django.contrib.auth.decorators import login_required

def detail_project(request,project_id):
    News = get_object_or_404(Project,pk=project_id).news_set.order_by('-date')[:5]
    project = get_object_or_404(Project,pk=project_id)
    return direct_to_template(request=request, template='index.html', extra_context={'News':News,
                                                                                     'project':project,
                                                                                     'project_id':project_id,
                                                                                     })

def detail_news(request,project_id,news_id):
    news = get_object_or_404(get_object_or_404(Project,pk=project_id).news_set,pk=news_id)
    project = get_object_or_404(Project,pk=project_id)
    return direct_to_template(request=request, template='detail_news.html', extra_context={'news':news,
                                                                                           'project':project,
                                                                                           })
@login_required
def add_news(request,project_id):
    user=request.user
    project = get_object_or_404(Project,pk=project_id)
    form = ''
    if request.method == 'POST':
        form = AddNewsForm(request.POST or None)
        if (user in project.admins.all() or user in project.moders.all()):
            if form.is_valid():
                n=form.save(commit=False)
                n.user = user
                project.news_set.add(n)
                return redirect("/project/%d/" % (int(project_id)))
    else:
        form = AddNewsForm()
    return direct_to_template(request=request, template='add_news.html', extra_context={'form':form,
                                                                                        'project':project,
                                                                                        'user':user,
                                                                                        })
@login_required
def new_project(request):
    user = request.user
    form = ''
    if request.method == 'POST':
        form = AddProjectForm(request.POST or None)
        if form.is_valid():
            tags = form.cleaned_data['_tags'].split()
            p = form.save()
            for i in tags:
                t = Tag.objects.get_or_create(text=i)[0]
                t.save()
                p.tags.add(t)
            return redirect('/account/')
    else:
        form = AddProjectForm()
    return direct_to_template(request, 'add_project.html', locals())

def list_project_by_tag(request,tag):
    t = get_object_or_404(Tag,text=tag)
    projects = t.projects.all()
    return direct_to_template(request, 'list_projects.html', locals())