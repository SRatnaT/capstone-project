# flake8: noqa

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_project_update_triggers_notification(auth_client, project, mocker):

    # Mocking the http pOST request

    mocked_post = mocker.patch("api.views.requests.post")

    # URL to create Project

    url = reverse("project-list")

    # Make Test Project request api call

    response = auth_client.post(
        url, data={"name": "New Test Project", "description": "New Test Description"}, format="json"
    )

    assert response.status_code == 201

    mocked_post.assert_called_once()

    args, kwargs = mocked_post.call_args

    assert args[0] == "http://localhost:8080/broadcast"
    assert kwargs["json"]["event"] == "PROJECT CREATED"
    assert kwargs["json"]["data"]["name"] == "New Test Project"
    assert kwargs["json"]["data"]["description"] == "New Test Description"
