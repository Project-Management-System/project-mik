from django.db import models
from Projects.models import Project

class WikiPage(models.Model):
    project = models.ForeignKey(Project,related_name='wiki')
    title = models.CharField(max_length=50,primary_key=True)
    text = models.TextField()
