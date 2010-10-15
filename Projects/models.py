from django.db import models
from django.contrib.auth.models import User
import datetime

class Tag(models.Model):
    text = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.text

class Project(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank= True)
    admins = models.ManyToManyField(User,related_name = 'admin_project')
    moders = models.ManyToManyField(User,related_name = 'moder_project',blank = True)
    tags = models.ManyToManyField(Tag,related_name = 'projects',blank = True)
    date_started = models.DateField(default = datetime.datetime.now())
    is_open = models.BooleanField(default = True)
    licence = models.CharField(blank=True,max_length=50)
#    last_edit = models.DateField(default = datetime.datetime.now())
    
    def __unicode__(self):
        return self.name
    
class News(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    date = models.DateTimeField(default = datetime.datetime.now())
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    
    class Meta:
        get_latest_by = 'date'
    
    def __unicode__(self):
        return self.title[:20]
    
class Downloads(models.Model):
    file = models.FilePathField()
    project = models.ForeignKey(Project)