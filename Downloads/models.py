from django.db import models
from Projects.models import Project
from django.contrib.auth.models import User
import datetime

class File(models.Model):
    project = models.ForeignKey(Project,related_name='files')
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    uploader = models.ForeignKey(User)
    datetime = models.DateTimeField(default=datetime.datetime.now())
    
    def __unicode__(self):
        return self.name