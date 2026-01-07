# flake8: noqa

import django
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

from api.models import Project, Task

django.setup()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="testpass123")


@pytest.fixture
def auth_client(api_client, user):

    # Removing the need for any kind of authentication for the test user
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def project(user):

    return Project.objects.create(name="Test Project", description="Test Description", owner=user)


@pytest.fixture
def task(project, user):

    return Task.objects.create(
        title="Test Task", description="Test Task Description", is_completed=True, project=project, owner=user
    )
