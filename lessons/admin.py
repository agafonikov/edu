from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import UserProfile, Course
from . import models

# Register your models here.
@admin.register(UserProfile)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": (
            "email",
            "password",
        )}),
        ("Personal info", {"fields": (
            "first_name",
            "second_name",
        )}),
        ("Permissions", {"fields": (
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )}),
        (
            "Dates", {"fields": (
                "last_login",
                "date_joined",
            )}
        )
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        })
    )
    list_display = (
        "email",
        "first_name",
        "second_name",
        "is_staff",
    )
    search_fields = ("email", "first_name", "second_name")
    ordering = ("email",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    filter_horizontal = ('moderators',)


@admin.register(models.CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'course')
    ordering = ['priority']
