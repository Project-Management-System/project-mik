from django import forms
from the_project.Projects.models import News

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'text')