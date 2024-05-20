from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField()


class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, verbose_name='Start Date')
    end_date = models.DateField(blank=True, null=True, verbose_name='End Date')
    description = models.TextField()


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField(blank=True, null=True)  # Allow null values
    end_date = models.DateField(blank=True, null=True)


class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    organization = models.CharField(max_length=100)
    date_earned = models.DateField()


@receiver(pre_save, sender=Certification)
def set_certification_user(sender, instance, **kwargs):
    if not instance.user_id:
        instance.user = instance.user


class PortfolioItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE, blank=True, null=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE, blank=True, null=True)
    certifications = models.ManyToManyField(Certification)
