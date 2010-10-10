from django import forms
from the_project.Tickets.models import Comment

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)