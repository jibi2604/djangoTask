# urls.py in the portfolio app

from django.urls import path
from . import views
app_name = 'portfolio'

urlpatterns = [
    # Project URLs
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/update/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),

    # Work Experience URLs
    path('work-experience/', views.WorkExperienceListView.as_view(), name='work_experience_list'),
    path('work-experience/create/', views.WorkExperienceCreateView.as_view(), name='work_experience_create'),
    path('work-experience/<int:pk>/', views.WorkExperienceDetailView.as_view(), name='work_experience_detail'),
    path('work-experience/<int:pk>/update/', views.WorkExperienceUpdateView.as_view(), name='work_experience_update'),
    path('work-experience/<int:pk>/delete/', views.WorkExperienceDeleteView.as_view(), name='work_experience_delete'),

    # Education URLs
    path('education/', views.EducationListView.as_view(), name='education_list'),
    path('education/create/', views.EducationCreateView.as_view(), name='education_create'),
    path('education/<int:pk>/', views.EducationDetailView.as_view(), name='education_detail'),
    path('education/<int:pk>/update/', views.EducationUpdateView.as_view(), name='education_update'),
    path('education/<int:pk>/delete/', views.EducationDeleteView.as_view(), name='education_delete'),

    # Certification URLs
    path('certifications/', views.CertificationListView.as_view(), name='certification_list'),
    path('certifications/create/', views.CertificationCreateView.as_view(), name='certification_create'),
    path('certifications/<int:pk>/', views.CertificationDetailView.as_view(), name='certification_detail'),
    path('certifications/<int:pk>/update/', views.CertificationUpdateView.as_view(), name='certification_update'),
    path('certifications/<int:pk>/delete/', views.CertificationDeleteView.as_view(), name='certification_delete'),
]
