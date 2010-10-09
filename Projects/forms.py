from django import forms

class AddNewsForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget = forms.Textarea)