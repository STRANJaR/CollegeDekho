# Generated by Django 5.0.2 on 2024-04-09 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_remove_college_profile_id_college_profile_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='access_token',
            field=models.CharField(default='', max_length=100),
        ),
    ]