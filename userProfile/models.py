from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
    SKILL_CHOICES = [
        ('Programming', 'Programming'),
        ('Graphic Design', 'Graphic Design'),
        ('Others', 'Others'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=True)
    skills = models.CharField(max_length=100, blank=True, choices=SKILL_CHOICES)
    contact_details = models.CharField(max_length=100, blank=True)

    def get_full_name(self):
        return self.user.get_full_name()
