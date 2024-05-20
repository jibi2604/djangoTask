from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    demo_link = models.URLField()
    github_link = models.URLField()

    def __str__(self):
        return self.title

