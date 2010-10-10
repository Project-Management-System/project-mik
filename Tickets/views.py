# Create your views here.
from the_project.Projects.models import Project
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.simple import direct_to_template
from django.http import HttpResponse
from the_project.Tickets.forms import AddComment

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
        form = AddComment(request.POST)
        if form.is_valid() and user.is_authenticated():
            c = form.save(commit=False)
            c.user = user
            ticket.comment_set.create(c)
            return redirect('/project/%s/tickets/%s/' % (project_id,ticket_id))
    else:
        form = AddComment()
    comments = ticket.comment_set.all()
    return direct_to_template(request=request, template='detail_ticket.html', extra_context=locals())