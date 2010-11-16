from django import forms
from Downloads.models import File

class UploadForm(forms.ModelForm):
    file = forms.FileField()
    class Meta:
        model = File
        fields = ('comment',)