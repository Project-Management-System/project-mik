from django import forms
from Tickets.models import Comment,Ticket

TICKET_TYPES = (
                ('Bug','Bug'),
                ('Critical Bug','Critical Bug'),
                ('Security Bug','Security Bug'),
                ('feature-request','feature-request'),
                )

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        
class AddTicket(forms.Form):
    name = forms.CharField()
    type = forms.CharField(widget = forms.Select(choices = TICKET_TYPES))
    text = forms.CharField(widget = forms.Textarea)