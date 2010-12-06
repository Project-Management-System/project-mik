from django import forms
from Tickets.models import Comment,Ticket
import Tickets

TICKET_TYPES = (
                ('Bug','Bug'),
                ('Critical Bug','Critical Bug'),
                ('Security Bug','Security Bug'),
                ('feature-request','feature-request'),
                )

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        
class AddTicketForm(forms.Form):
    name = forms.CharField()
    type = forms.CharField(widget = forms.Select(choices = TICKET_TYPES))
    text = forms.CharField(widget = forms.Textarea)
    
class EditTicketForm(forms.ModelForm):
    type = forms.CharField(widget = forms.Select(choices = TICKET_TYPES))
    class Meta:
        model = Ticket
        fields = ('name','status','description')
