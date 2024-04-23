# Generated by Django 5.0.2 on 2024-04-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_jobpost_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='failed_login_attempts',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='college',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='college',
            name='locked_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
