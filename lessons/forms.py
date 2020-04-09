from django.contrib.auth.forms import (
    UserCreationForm as DjangoUserCreationForm,
)
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import authenticate
from django import forms
from . import models

import logging

logger = logging.getLogger(__name__)


class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = models.UserProfile
        fields = ("email", "first_name", "second_name")
        field_classes = {"email": UsernameField}


class AuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        strip=False, widget=forms.PasswordInput
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password1")

        if email is not None and password:
            self.user = authenticate(
                self.request,
                email=email,
                password=password,
            )
            if self.user is None:
                raise forms.ValidationError(
                    "Invalid email or password."
                )
            logger.info(
                "Authentication successful for email: %s", email
            )
        return self.cleaned_data

    def get_user(self):
        return self.user


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ('name', 'icon')

    def __init__(self, *args, **kwargs):
        super(CourseCreationForm, self).__init__(*args, **kwargs)
        self.fields['icon'].required = False
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(False)
        commit and obj.save()
        return obj


class ModuleCreationForm(forms.ModelForm):
    class Meta:
        model = models.CourseModule
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(ModuleCreationForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(False)
        commit and obj.save()
        return obj


class LessonCreationForm(forms.ModelForm):
    class Meta:
        model = models.Lesson
        fields = ('name', 'description', 'presentation_link', 'lesson_link')

    def __init__(self, *args, **kwargs):
        super(LessonCreationForm, self).__init__(*args, **kwargs)
        self.fields['description']      .required = False
        self.fields['presentation_link'].required = False
        self.fields['lesson_link']      .required = False
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super().save(False)
        commit and obj.save()
        return obj