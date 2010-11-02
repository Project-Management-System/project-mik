from django.shortcuts import get_object_or_404, redirect
from wiki.models import WikiPage
from django.views.generic.simple import direct_to_template
from Projects.models import Project
from wiki.forms import WikiForm
from django.contrib.markup.templatetags.markup import textile

def view_page(request, page_name,project_id):
    project = get_object_or_404(Project,pk=project_id)
    try:
        page =  project.wiki.get(pk=page_name)
        page.text = textile(page.text)
    except WikiPage.DoesNotExist:
        pass
    return direct_to_template(request, 'wiki/main.html', locals())

def edit_page(request,page_name,project_id):
    project = get_object_or_404(Project,pk=project_id)
    try:
        page = project.wiki.get(pk=page_name)
        form = WikiForm(instance=page)
    except WikiPage.DoesNotExist:
        form = WikiForm()
    if request.method == 'POST':
        text = request.POST.get('text',None)
        if text:
            page = WikiPage(title=page_name,text=text,project=project)
            page.save()
            return redirect('/project/%s/wiki/%s/'%(project_id,page_name))
    return direct_to_template(request, 'wiki/edit.html', locals())