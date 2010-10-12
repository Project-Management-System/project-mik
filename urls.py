from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$','the_project.Projects.views.detail_project',{'project_id':1}),
    (r'^news/(?P<news_id>\d+)/$','the_project.Projects.views.detail_news',{'project_id':1}),
    (r'^users/(?P<user_id>\d+)/$','the_project.views.detail_user'),
    
    (r'^project/(?P<project_id>\d+)/news/add/$','the_project.Projects.views.add_news'),
    (r'^project/(?P<project_id>\d+)/$','the_project.Projects.views.detail_project'),
    (r'^project/(?P<project_id>\d+)/news/(?P<news_id>\d+)/$','the_project.Projects.views.detail_news'),
    (r'^project/(?P<project_id>\d+)/tickets/$','the_project.Tickets.views.list_tickets'),
    (r'^project/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/$','the_project.Tickets.views.detail_ticket'),
    (r'^project/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/add/$','the_project.Tickets.views.detail_ticket'),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/home/mik/Aptana Studio 3 Workspace/the_project/src/the_project/media/'}),
#    (r'^account/', include('registration.urls')),
    (r'^account/register/$','the_project.UserProfile.views.register'),
    (r'^account/$','the_project.UserProfile.views.account'),
    (r'^account/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    (r'^account/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^account/messages$', 'the_project.UserProfile.views.messages'),
    (r'^account/messages/(?P<message_id>\d+)', 'the_project.UserProfile.views.detail_message'),
    (r'^account/messages/send/$', 'the_project.UserProfile.views.send_message'),
)