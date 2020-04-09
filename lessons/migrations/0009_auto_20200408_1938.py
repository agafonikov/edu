# Generated by Django 3.0.4 on 2020-04-08 19:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0008_auto_20200408_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='moderators',
            field=models.ManyToManyField(blank=True, related_name='managing_courses', to=settings.AUTH_USER_MODEL),
        ),
    ]