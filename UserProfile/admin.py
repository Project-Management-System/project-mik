from django.contrib import admin
from the_project.UserProfile.models import UserProfile, Message

admin.site.register(UserProfile)
admin.site.register(Message)