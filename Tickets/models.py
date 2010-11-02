from django.db import models
from Projects.models import Project
import datetime
from django.contrib.auth.models import User

class Ticket(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    project = models.ForeignKey(Project)
    type = models.CharField(max_length = 20)
    status = models.CharField(max_length = 20,default = 'new')
    submitted = models.DateTimeField(default = datetime.datetime.now())
    user = models.ForeignKey(User)
    priority = models.IntegerField(default = 5)
    
    def __unicode__(self):
        return self.name
    
class Comment(models.Model):
    datetime = models.DateField(default = datetime.datetime.now())
    text = models.TextField()
    user = models.ForeignKey(User)
    ticket = models.ForeignKey(Ticket)
    
    def __unicode__(self):
        return str(self.ticket)+': '+ self.text[:20]