from django import forms

class AddComment(forms.Form):
    text = forms.CharField(widget = forms.Textarea)