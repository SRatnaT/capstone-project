# flake8: noqa

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_task_update_triggers_notification(auth_client, task, mocker):

    # Mocking the requests.post HTTP request call

    mocked_post = mocker.patch("api.views.requests.post")

    # URL to hit for PATCH to update a task

    url = reverse("task-detail", args=[task.id])

    # Make PATCH Call to the test db

    response = auth_client.patch(url, data={"title": "Updated task"}, format="json")

    assert response.status_code == 200

    mocked_post.assert_called_once()

    args, kwargs = mocked_post.call_args

    assert args[0] == "http://localhost:8080/broadcast"
    assert kwargs["json"]["event"] == "TASK UPDATED"
    assert kwargs["json"]["data"]["title"] == "Updated task"
