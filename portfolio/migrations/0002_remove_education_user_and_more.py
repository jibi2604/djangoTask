# Generated by Django 4.2.11 on 2024-05-02 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='user',
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='certifications',
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='education',
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='project',
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='portfolioitem',
            name='work_experience',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='user',
        ),
        migrations.DeleteModel(
            name='Certification',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='PortfolioItem',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
    ]
