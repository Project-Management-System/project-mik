from django.shortcuts import get_object_or_404, redirect
from Projects.models import Project
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from Downloads.forms import UploadForm
import os

@login_required
def list_files(request,project_id):
    project = get_object_or_404(Project,pk=project_id)
    is_admin = project.is_admin(request.user)
    is_moder = project.is_moder(request.user)
    return direct_to_template(request, 'downloads/list.html', locals())

@login_required
def upload(request,project_id):
    project = get_object_or_404(Project,pk=project_id)
    is_admin = project.is_admin(request.user)
    is_moder = project.is_moder(request.user)
    if request.method == 'POST' and is_moder:
        form = UploadForm(request.POST or None)
        file = request.FILES.get('file',None)
        print request.FILES
        if file:
            if not os.path.exists('media/files/%s/%s'%(project.id,file.name)):
                if not os.path.exists('media/files/%s/'%(project.id)):
                    os.mkdir('media/files/%s/'%(project.id))
                dest = open('media/files/%s/%s'%(project.id,file.name),'wb+')
                for c in file.chunks():
                    dest.write(c)
                dest.close()
                project.files.create(name=file.name,project=project,comment=form.data['comment'],uploader=request.user)
                project.news_set.create(title='File uploaded: %s'%(file.name),text=form.data['comment'],user=request.user)
                return redirect('/project/%s/files/'%(project_id))
    else:
        form = UploadForm()
    return direct_to_template(request, 'downloads/upload.html', locals())

@login_required
def delete(request,project_id,file_name):
    project = get_object_or_404(Project,pk=project_id)
    is_admin = project.is_admin(request.user)
    is_moder = project.is_moder(request.user)
    if is_moder:
        file = get_object_or_404(project.files,name=file_name)
        try:
            os.remove('media/files/%s/%s'%(project_id,file_name))
        except:
            pass
        file.delete()
    return redirect('/project/%s/files/'%(project_id))