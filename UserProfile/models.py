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
    
    def num_new_messages(self):
        return self.user.inbox.filter(is_new=True).count()
    
    def __unicode__(self):
        return str(self.user)
    
class Message(models.Model):
    subject = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default = datetime.now())
    from_user = models.ForeignKey(User,related_name='outbox')
    to_user = models.ForeignKey(User,related_name='inbox')
    is_new = models.BooleanField(default = True)
    
    def __unicode__(self):
        return str(self.from_user) + ' -> ' + str(self.to_user)