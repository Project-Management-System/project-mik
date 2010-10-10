from django.views.generic.simple import direct_to_template
from the_project.Projects.models import Project, News
from the_project.forms import LoginForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import Http404
from the_project.Projects.forms import AddNewsForm
from django.contrib.auth.decorators import login_required


def short_text(x):
        x.text=x.text[:100]+'...'
        return x

def detail_project(request,project_id):
    News = map(short_text,get_object_or_404(Project,pk=project_id).news_set.order_by('-date')   )
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
    error=str()
    user=request.user
    project = get_object_or_404(Project,pk=project_id)
    if request.method == 'POST':
        title = request.POST.get('title',None)
        text = request.POST.get('text',None)
        if (user in project.admins.all() or user in project.moders.all()):
            if title and text:
                project.news_set.add(News(title=title,text=text,user=user))
                return redirect("/project/%d/" % (int(project_id)))
            else:
                error = 'Please fill Title and Text.'
        else:
            error = 'You do not have permissions to post news'
    form = AddNewsForm(request.POST or None)
    return direct_to_template(request=request, template='add_news.html', extra_context={'form':form,
                                                                                        'project':project,
                                                                                        'user':user,
                                                                                        'error':error
                                                                                        })