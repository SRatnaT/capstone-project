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
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api.views import (  # CommentDetailView,; MemberDetailView,
    CommentViewSet,
    MemberViewSet,
    ProjectDetailView,
    ProjectListCreateView,
    ProjectViewSet,
    TaskDetailView,
    TaskListCreateView,
    TaskViewSet,
)

from .views import home

schema_view = get_schema_view(
    openapi.Info(
        title="Capstone Project API",
        default_version="v1",
        description="API documentation for Capstone Project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")
router.register(r"projects", ProjectViewSet, basename="project")
router.register(r"comments", CommentViewSet, basename="comment")
router.register(r"members", MemberViewSet, basename="member")

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", obtain_auth_token),
    path("swagger<str:format>", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc-ui"),
    # API app URLs
    path("api/", include(router.urls)),
    # Example for usage of Router URL
    # - tasks/ -> all object instances of tasks
    # - tasks/1/ -> first instance of tasks
    # Tasks Model URLs
    # path("tasks/", TaskListCreateView.as_view(), name="task-list-create"),
    # path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    # Project Model URLS
    # path("projects/", ProjectListCreateView.as_view(), name="project-detail"),
    # path("projects/<int:pk>/", ProjectDetailView.as_view(), name="task-detail"),
]
