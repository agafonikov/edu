from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth import views as auth_views
from . import views
from . import forms


lessonurls = [
    path('create/', views.create_lesson),
    path('<int:pk_lesson>/', views.LessonDetailView.as_view(template_name='lesson_detail.html')),
]

moduleurls = [
    path('create/', views.create_module),
    path('<int:pk_module>/', views.ModuleDetailView.as_view(template_name="module_detail.html")),
    path('<int:pk_module>/lesson/', include(lessonurls)),
]

courseurls = [
    path('<int:pk>/', views.CourseDetailView.as_view(template_name="course_detail.html")),
    path('<int:pk>/module/', include(moduleurls)),
    path('create/', views.create_course,),
]

urlpatterns = [
    path('', views.CourseListView.as_view(template_name='course_list.html'), name='index'),
    path('profile/<int:pk>/', views.ProfileView.as_view(template_name='profile.html')),
    path('profile/', views.ProfileView.as_view(template_name='profile.html')),
    path('signup/', views.SignUpView.as_view()),
    path('signin/', auth_views.LoginView.as_view(
        template_name="login.html",
        form_class=forms.AuthenticationForm
    ),
         name="login"),
    path('course/', include(courseurls)),
]
