from django import forms
from .models import Project, WorkExperience, Education, Certification


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['company', 'position', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD-MM-YYYY'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD-MM-YYYY'}),
        }


class EducationForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(format='%d-%m-%y'))
    end_date = forms.DateField(widget=forms.DateInput(format='%d-%m-%y'))

    class Meta:
        model = Education
        fields = ['institution', 'degree', 'field_of_study', 'start_date', 'end_date']


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['title', 'organization', 'date_earned', 'issue_date']
