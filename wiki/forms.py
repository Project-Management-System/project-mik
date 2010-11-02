from django import forms
from wiki.models import WikiPage

class WikiForm(forms.ModelForm):
    class Meta:
        model = WikiPage
        fields = ('text',)