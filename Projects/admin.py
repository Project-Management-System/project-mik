from django.contrib import admin
from Projects.models import Project, Tag, News
from django import forms

admin.site.register(Tag)
admin.site.register(News)
admin.site.register(Project)