# Generated by Django 3.0.4 on 2020-04-08 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0009_auto_20200408_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='first_module',
        ),
        migrations.RemoveField(
            model_name='coursemodule',
            name='first_lesson',
        ),
        migrations.RemoveField(
            model_name='coursemodule',
            name='next_module',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='next_lesson',
        ),
        migrations.AddField(
            model_name='coursemodule',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='lessons.Course'),
        ),
        migrations.AddField(
            model_name='coursemodule',
            name='priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='lessons.CourseModule'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]
