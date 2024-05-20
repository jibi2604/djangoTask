# views.py in the portfolio app

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project, WorkExperience, Education, Certification
from .forms import ProjectForm, WorkExperienceForm, EducationForm, CertificationForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Project views
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'portfolios/project_list.html'
    context_object_name = 'projects'


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'portfolios/project_detail.html'
    context_object_name = 'project'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolios/project_form.html'
    success_url = reverse_lazy('portfolio:project_list')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'portfolios/project_update.html'
    success_url = reverse_lazy('portfolio:project_list')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'portfolios/project_confirm_delete.html'
    success_url = reverse_lazy('portfolio:project_list')


# Work Experience views

class WorkExperienceListView(LoginRequiredMixin, ListView):
    model = WorkExperience
    template_name = 'portfolios/work_experience_list.html'
    context_object_name = 'work_experiences'

    def get_queryset(self):
        return WorkExperience.objects.filter(user=self.request.user)


class WorkExperienceDetailView(LoginRequiredMixin, DetailView):
    model = WorkExperience
    template_name = 'portfolios/work_experience_detail.html'
    context_object_name = 'work_experience'


class WorkExperienceCreateView(LoginRequiredMixin, CreateView):
    model = WorkExperience
    fields = ['company', 'position', 'start_date', 'end_date',
              'description']
    template_name = 'portfolios/work_experience_form.html'
    success_url = reverse_lazy('portfolio:work_experience_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WorkExperienceUpdateView(LoginRequiredMixin, UpdateView):
    model = WorkExperience
    fields = ['company', 'position', 'start_date', 'end_date',
              'description']  # Specify fields to include in the form
    template_name = 'portfolios/work_experience_form.html'
    success_url = reverse_lazy('portfolio:work_experience_list')


class WorkExperienceDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkExperience
    template_name = 'portfolios/work_experience_confirm_delete.html'
    success_url = reverse_lazy('portfolio:work_experience_list')


# Education views
class EducationListView(LoginRequiredMixin, ListView):
    model = Education
    template_name = 'portfolios/education_list.html'
    context_object_name = 'educations'


class EducationDetailView(LoginRequiredMixin, DetailView):
    model = Education
    template_name = 'portfolios/education_detail.html'
    context_object_name = 'educations'


class EducationCreateView(LoginRequiredMixin, CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'portfolios/education_form.html'
    success_url = reverse_lazy('portfolio:education_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EducationUpdateView(LoginRequiredMixin, UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'portfolios/education_form.html'
    success_url = reverse_lazy('portfolio:education_list')


class EducationDeleteView(LoginRequiredMixin, DeleteView):
    model = Education
    template_name = 'portfolios/education_confirm_delete.html'
    success_url = reverse_lazy('portfolio:education_list')


# Certification views
class CertificationListView(LoginRequiredMixin, ListView):
    model = Certification
    template_name = 'portfolios/certification_list.html'
    context_object_name = 'certifications'


class CertificationDetailView(LoginRequiredMixin, DetailView):
    model = Certification
    template_name = 'portfolios/certification_detail.html'
    context_object_name = 'certification'


class CertificationCreateView(LoginRequiredMixin, CreateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'portfolios/certification_form.html'
    success_url = reverse_lazy('portfolio:certification_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CertificationUpdateView(LoginRequiredMixin, UpdateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'portfolios/certification_form.html'
    success_url = reverse_lazy('portfolio:certification_list')


class CertificationDeleteView(LoginRequiredMixin, DeleteView):
    model = Certification
    template_name = 'portfolios/certification_confirm_delete.html'
    success_url = reverse_lazy('portfolio:certification_list')
