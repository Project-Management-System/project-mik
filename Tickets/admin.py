from django.contrib import admin
from the_project.Tickets.models import Ticket, Comment

admin.site.register(Ticket)
admin.site.register(Comment)