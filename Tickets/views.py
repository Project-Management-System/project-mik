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
    project = get_object_or_404(Project,pk=project_id)
    ticket = get_object_or_404(project.ticket_set,pk=ticket_id)
    if request.method == 'POST':
        text = request.POST.get('text', None)
        user = request.user
        if text and user.is_authenticated():
            ticket.comment_set.create(text=text,user=user)
            return redirect('/project/%d/tickets/%d' % (int(project_id),int(ticket_id)))
    else:
        comments = ticket.comment_set.all()
        form = AddComment()
        return direct_to_template(request=request, template='detail_ticket.html', extra_context=locals())