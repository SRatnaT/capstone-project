import cProfile
import os
import sys

import django
from django.contrib.auth import get_user_model
from django.test import Client

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstoneDjango.settings")
django.setup()

User = get_user_model()


def run():

    client = Client()

    user = User.objects.get(username="sailtuladhar")

    client.force_login(user)

    payload = {
        "name": "Profiling Test Project",
        "description": "Testing cProfile on POST",
    }

    client.post("/api/projects/", payload, content_type="application/json")


cProfile.run("run()", sort="cumulative"),
