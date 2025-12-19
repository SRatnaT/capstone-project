# flake8: noqa

"""
URL configuration for capstoneDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from api.views import (  # CommentDetailView,; MemberDetailView,
    ProjectDetailView,
    ProjectListCreateView,
    TaskDetailView,
    TaskListCreateView,
)

from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    # Task Model URLS
    path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    # Project Model URLS
    path("projects/", ProjectListCreateView.as_view(), name="project-detail"),
    path("projects/<int:pk>/", ProjectDetailView.as_view(), name="task-detail"),
]
