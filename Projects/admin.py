from django.contrib import admin
from the_project.Projects.models import Project, Tag, News
from django import forms

admin.site.register(Tag)
admin.site.register(News)
admin.site.register(Project)