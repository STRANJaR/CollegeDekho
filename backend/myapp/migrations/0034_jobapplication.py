# Generated by Django 5.0.2 on 2024-04-11 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_rename_college_jobpost_college_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='resume/')),
                ('cover_letter', models.CharField(max_length=200)),
                ('faculty_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.faculty_profile')),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.jobpost')),
            ],
        ),
    ]