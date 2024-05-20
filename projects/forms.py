from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'demo_link', 'github_link']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter project title'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter project description'})
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['demo_link'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter demo link'})
        self.fields['github_link'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter GitHub link'})
