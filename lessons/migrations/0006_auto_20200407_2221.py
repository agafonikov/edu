# Generated by Django 3.0.4 on 2020-04-07 22:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_auto_20200407_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='icon',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='course icon'),
        ),
        migrations.AlterField(
            model_name='course',
            name='moderators',
            field=models.ManyToManyField(blank=True, null=True, related_name='course_name', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=32, verbose_name='course name'),
        ),
    ]