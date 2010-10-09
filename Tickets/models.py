from django.db import models
from the_project.Projects.models import Project
import datetime
from django.contrib.auth.models import User

class Ticket(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 10000)
    project = models.ForeignKey(Project)
    type = models.CharField(max_length = 20)
    status = models.CharField(max_length = 20)
    datetime_started = models.DateTimeField(default = datetime.datetime.now())
    
    def __unicode__(self):
        return self.name+'(id='+str(self.pk)+')'
    
class Comment(models.Model):
    datetime = models.DateField(default = datetime.datetime.now())
    text = models.TextField()
    user = models.ForeignKey(User)
    ticket = models.ForeignKey(Ticket)
    
    def __unicode__(self):
        return str(self.ticket)+': '+ self.text[:20]