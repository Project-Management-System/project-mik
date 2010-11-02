# Create your views here.
from Projects.models import Project
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.simple import direct_to_template
from Tickets.forms import AddCommentForm, AddTicketForm, EditTicketForm
from django.contrib.auth.decorators import login_required

def list_tickets(request,project_id):
    project = get_object_or_404(Project,pk=project_id)
    tickets = project.ticket_set.all()
    is_admin = project.is_admin(request.user)
    is_moder = project.is_moder(request.user)
    return direct_to_template(request=request, template='list_tickets.html', extra_context=locals())

def detail_ticket(request,project_id,ticket_id):
    project = get_object_or_404(Project,pk=project_id)
    ticket = get_object_or_404(project.ticket_set,pk=ticket_id)
    user = request.user
    if request.method == 'POST':
        form = AddCommentForm(request.POST or None)
        text = request.POST.get('text',None)
        if text and user.is_authenticated():
            ticket.comment_set.create(user=user, text=text)
            return redirect('/project/%s/tickets/%s/' % (project_id,ticket_id))
    else:
        form = AddCommentForm()
    comments = ticket.comment_set.all()
    is_admin = project.is_admin(request.user)
    is_moder = project.is_moder(request.user)
    return direct_to_template(request=request, template='detail_ticket.html', extra_context=locals())

@login_required
def add_ticket(request,project_id):
    project = get_object_or_404(Project,pk=project_id)
    user = request.user
    if request.method == 'POST':
        form = AddTicketForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            type = form.cleaned_data['type']
            t = project.ticket_set.create(name=name,type=type)
            t.comment_set.create(text=text,user=user)
            return redirect('/project/%s/tickets/'%(project_id))
    else:
        form = AddTicketForm()
    is_admin = project.is_admin(request.user)
    is_moder = project.is_moder(request.user)
    return direct_to_template(request, 'add_ticket.html', locals())

@login_required
def edit_ticket(request,project_id,ticket_id):
    project = get_object_or_404(Project,pk=project_id)
    ticket = get_object_or_404(project.ticket_set,pk=ticket_id)
    user = request.user
    if request.method == 'POST':
        form = EditTicketForm(request.POST or None,instance=ticket)
        if form.is_valid() and project.is_moder(user):
            form.save()
            return redirect('/project/%s/tickets/%s/'%(project_id,ticket_id))
    else:
        form = EditTicketForm(instance=ticket)
    is_admin = project.is_admin(request.user)
    is_moder = project.is_moder(request.user)
    return direct_to_template(request, 'edit_ticket.html', locals())

@login_required
def delete_ticket(request,project_id,ticket_id):
    project = get_object_or_404(Project,pk=project_id)
    ticket = get_object_or_404(project.ticket_set,pk=ticket_id)
    user = request.user
    if project.is_moder(user):
        ticket.delete()
        return redirect('/project/%s/tickets/'%(project_id))
    return redirect('/project/%s/tickets/%s/'%(project_id,ticket_id))

@login_required
def delete_comment(request,project_id,ticket_id,comment_id):
    project = get_object_or_404(Project,pk=project_id)
    ticket = get_object_or_404(project.ticket_set,pk=ticket_id)
    comment = get_object_or_404(ticket.comment_set,pk=comment_id)
    user = request.user
    if project.is_moder(user):
        comment.delete()
        return redirect('/project/%s/tickets/%s/'%(project_id,ticket_id))
    redirect('/project/%s/tickets/%s/'%(project_id,ticket_id))