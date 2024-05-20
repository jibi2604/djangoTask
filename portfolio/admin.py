from django.contrib import admin
from portfolio.models import Project, WorkExperience, Education, Certification, PortfolioItem

# Register your models here.
admin.site.register(Project)
admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Certification)
admin.site.register(PortfolioItem)
