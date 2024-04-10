# Generated by Django 5.0.2 on 2024-04-10 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_alter_college_access_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='college_profile',
            name='created_date',
            field=models.DateField(auto_now=True),
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
                ('description', models.TextField(null=True)),
                ('vacancy_available', models.IntegerField(default=1)),
                ('skills_required', models.TextField(max_length=500, null=True)),
                ('about_work', models.TextField(max_length=500)),
                ('who_can_apply', models.TextField(max_length=300)),
                ('additional_information', models.TextField(max_length=200, null=True)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.college_profile')),
            ],
        ),
    ]