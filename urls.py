from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$','Projects.views.detail_project',{'project_id':1}),
    (r'^news/(?P<news_id>\d+)/$','Projects.views.detail_news',{'project_id':1}),
    (r'^users/(?P<user_id>\d+)/$','views.detail_user'),
    
    (r'^project/(?P<project_id>\d+)/news/add/$','Projects.views.add_news'),
    (r'^project/(?P<project_id>\d+)/$','Projects.views.detail_project'),
    (r'^project/(?P<project_id>\d+)/news/(?P<news_id>\d+)/$','Projects.views.detail_news'),
    (r'^project/(?P<project_id>\d+)/tickets/$','Tickets.views.list_tickets'),
    (r'^project/(?P<project_id>\d+)/tickets/add/$','Tickets.views.add_ticket'),
    (r'^project/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/$','Tickets.views.detail_ticket'),
    (r'^project/(?P<project_id>\d+)/tickets/(?P<ticket_id>\d+)/add/$','Tickets.views.detail_ticket'),
    (r'^project/new/','Projects.views.new_project'),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': 'media/'}),
#    (r'^account/', include('registration.urls')),
    (r'^account/register/$','UserProfile.views.register'),
    (r'^account/$','UserProfile.views.account'),
    (r'^account/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    (r'^account/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^account/messages/inbox/$', 'UserProfile.views.messages',{'type':'inbox'}),
    (r'^account/messages/outbox/$', 'UserProfile.views.messages',{'type':'outbox'}),
    (r'^account/messages/(?P<message_id>\d+)', 'UserProfile.views.detail_message'),
    (r'^account/messages/send/$', 'UserProfile.views.send_message'),
    
#    (r'^','django.views.generic.simple.redirect_to',{'url':'/'})
)