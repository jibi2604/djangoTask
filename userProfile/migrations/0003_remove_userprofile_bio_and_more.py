# Generated by Django 4.2.11 on 2024-05-02 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0002_alter_userprofile_contact_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='contact_details',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
