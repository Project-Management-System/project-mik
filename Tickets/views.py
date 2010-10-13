# Create your views here.
from Projects.models import Project
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.simple import direct_to_template
from django.http import HttpResponse
from Tickets.forms import AddComment, AddTicket
from django.contrib.auth.decorators import login_required

def list_tickets(request,project_id):
    project = get_object_or_404(Project,pk=project_id)
    tickets = project.ticket_set.all()
    return direct_to_template(request=request, template='list_tickets.html', extra_context=locals())

def detail_ticket(request,project_id,ticket_id):
    form = AddComment()
    project = get_object_or_404(Project,pk=project_id)
    ticket = get_object_or_404(project.ticket_set,pk=ticket_id)
    user = request.user
    if request.method == 'POST':
        text = request.POST.get('text',None)
        if text and user.is_authenticated():
            ticket.comment_set.create(user=user, text=text)
            return redirect('/project/%s/tickets/%s/' % (project_id,ticket_id))
    else:
        form = AddComment()
    comments = ticket.comment_set.all()
    return direct_to_template(request=request, template='detail_ticket.html', extra_context=locals())

@login_required
def add_ticket(request,project_id):
    project = get_object_or_404(Project,pk=project_id)
    user = request.user
    form = ''
    if request.method == 'POST':
        form = AddTicket(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            type = form.cleaned_data['type']
            t = project.ticket_set.create(name=name,type=type)
            t.comment_set.create(text=text,user=user)
            return redirect('/project/%s/tickets/'%(project_id))
    else:
        form = AddTicket()
    return direct_to_template(request, 'add_ticket.html', locals())