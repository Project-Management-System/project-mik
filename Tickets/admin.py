from django.contrib import admin
from Tickets.models import Ticket, Comment

admin.site.register(Ticket)
admin.site.register(Comment)