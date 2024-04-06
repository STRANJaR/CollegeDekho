# Generated by Django 5.0.2 on 2024-04-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_user_college'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college_profile',
            name='college_image',
        ),
        migrations.AddField(
            model_name='college_profile',
            name='avtar_url',
            field=models.URLField(blank=True),
        ),
    ]
