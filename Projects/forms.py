from django import forms
from Projects.models import News, Project

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'text')
        
class AddProjectForm(forms.ModelForm):
    _tags = forms.CharField(required=False)
    class Meta:
        model = Project
        fields = ('name','description','is_open','licence','admins','moders')