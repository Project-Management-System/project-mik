from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date

class UserProfile(models.Model):
    birthday = models.DateField(default = datetime.date(datetime.now()))
    country = models.CharField(max_length = 50)
    rating = models.IntegerField(default = 0)
    is_banned = models.BooleanField(default = False) # ? is_active ?
    user = models.ForeignKey(User,unique = True)
    icq = models.CharField(max_length = 9,blank = True)
    jabber = models.EmailField(blank = True)
    skype = models.CharField(max_length = 9,blank = True)
    
    def __unicode__(self):
        return str(self.user)