from django.db import models
from django.db.models import Model
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.dispatch import receiver


# Users profile class
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Insufficient data to create account')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                "SuperUser must have is_staff=True."
            )

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                "SuperUser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)


class UserProfile(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=32)
    second_name = models.CharField('second name', max_length=32)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first name', 'second name']

    objects = UserManager()


class Course(Model):
    creator = models.ForeignKey('UserProfile', on_delete=models.CASCADE, null=True, related_name='created_courses')
    moderators = models.ManyToManyField('UserProfile', blank=True, related_name='managing_courses')
    name = models.CharField('course name', max_length=32)
    description = models.TextField(null=True, blank=True)
    icon = models.ImageField('course icon', upload_to="static/images/", null=True, blank=True)


class CourseModule(Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='modules', null=True)
    priority = models.IntegerField(default=1)


class Lesson(Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    presentation_link = models.URLField(null=True)
    lesson_link = models.URLField(null=True)
    module = models.ForeignKey('CourseModule', on_delete=models.CASCADE, related_name='lessons', null=True)
    priority = models.IntegerField(default=1)
