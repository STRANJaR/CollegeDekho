# Generated by Django 5.0.3 on 2024-04-18 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_remove_college_profile_id_college_profile_college_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty_profile',
            name='id',
        ),
        migrations.AddField(
            model_name='college',
            name='access_token',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='college_profile',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='college_profile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='faculty_profile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='faculty_profile',
            name='faculty',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myapp.faculty'),
        ),
        migrations.AlterField(
            model_name='college_profile',
            name='description',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='college_profile',
            name='location',
            field=models.TextField(max_length=300),
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('vacancy_available', models.IntegerField(default=1)),
                ('skills_required', models.TextField(default='', max_length=500)),
                ('about_work', models.TextField(max_length=500)),
                ('who_can_apply', models.TextField(max_length=300)),
                ('additional_information', models.TextField(default='', max_length=200)),
                ('college_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.college_profile')),
            ],
        ),
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
