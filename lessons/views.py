from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import FormView, ListView, CreateView, DetailView
from django.shortcuts import get_object_or_404
from . import forms, models


import logging

logger = logging.getLogger(__name__)


class SignUpView(FormView):
    template_name = "signup.html"
    form_class = forms.UserCreationForm

    def get_success_url(self):
        redirect_to = self.request.GET.get("next", "/")
        return redirect_to

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get("password1")
        logger.info(
            "New signup for email = %s through SignUpView", email
        )
        user = authenticate(email=email, password=raw_password)
        login(self.request, user)

        messages.info(
            self.request,
            "You signed up successfully.",
        )
        return response


@login_required(login_url='signin/')
def create_course(request, **kwargs):
    form = forms.CourseCreationForm(request.POST)
    if request.method == 'POST':
        user = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = user
            obj.save()
        return HttpResponseRedirect("/")
    return render(request, "course_form.html", {'form': form})


@login_required(login_url='signin/')
def create_module(request, **kwargs):
    form = forms.ModuleCreationForm(request.POST)
    if request.method == 'POST':
        user = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.course = models.Course.objects.get(id=kwargs.get('pk'))
            obj.save()
        return HttpResponseRedirect("/")
    return render(request, "module_form.html", {'form': form})


@login_required(login_url='signin/')
def create_lesson(request, **kwargs):
    form = forms.LessonCreationForm(request.POST)
    if request.method == 'POST':
        user = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.module = models.CourseModule.objects.get(id=kwargs.get('pk_module'))
            obj.save()
        return HttpResponseRedirect("/")
    return render(request, "module_form.html", {'form': form})


class CourseListView(ListView):
    model = models.Course
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserListView(ListView):
    model = models.UserProfile
    paginate_by = 100

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProfileView(DetailView):
    model = models.UserProfile

    def get_object(self, queryset=None):
        user_id = self.kwargs.get(self.pk_url_kwarg, None)
        if self.kwargs.get(self.pk_url_kwarg, None):
            user = self.model.objects.get(id=user_id)
            return user
        else:
            user_id = self.request.user.id
            return get_object_or_404(self.model, id=user_id)


class CourseDetailView(DetailView):
    model = models.Course

    def get_object(self, queryset=None):
        course_id = self.kwargs.get(self.pk_url_kwarg, None)
        return get_object_or_404(self.model, id=course_id)


class ModuleDetailView(DetailView):
    model = models.CourseModule

    def get_object(self, queryset=None):
        model_id = self.kwargs.get('pk_module', None)
        return get_object_or_404(self.model, id=model_id)


class LessonDetailView(DetailView):
    model = models.Lesson

    def get_object(self, queryset=None):
        lesson_id = self.kwargs.get('pk_lesson', None)
        return get_object_or_404(self.model, id=lesson_id)
