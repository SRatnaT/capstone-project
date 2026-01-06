# from django.shortcuts import render

# flake8: noqa
import http.client
import json
from urllib.parse import urlparse

from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Comment, Member, Project, Task
from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, MemeberSerializer, ProjectSerializer, TaskSerializer

# Generic Class based Views


class TaskListCreateView(ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectListCreateView(ListCreateAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CommentDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class MemberDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Member.objects.all()
    serializer_class = MemeberSerializer


# View Sets

# class TaskViewSet(viewsets.ViewSet):

#     def list(self , request):

#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks , many = True)

#         return Response(serializer.data)

#     def create(self , request):

#         serializer = TaskSerializer(data = request.data)

#         if serializer.is_valid():

#             serializer.save()
#             return Response(serializer.data , status = 201)

#         return Response(serializer.errrors , status = 400)

#     def retrieve(self , request , pk = None):

#         # taskbyid = Task.objects.get(id = pk)
#         task = get_object_or_404(Task , pk = pk)
#         serializer = TaskSerializer(task)

#         return Response(serializer.data)


# ModelView Sets


class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)

        new_task = serializer.save()

        try:

            url = "http://localhost:8080/broadcast"
            parsed_url = urlparse(url)

            conn = http.client.HTTPConnection(parsed_url.hostname, parsed_url.port, timeout=2)

            payload = json.dumps({"event": "TASK CREATED", "data": TaskSerializer(new_task).data})

            headers = {"Content-Type": "application/json"}

            conn.request("POST", parsed_url.path, body=payload, headers=headers)
            response = conn.getresponse()

            print("TASK CREATED RES:", response)

            response.read()
            conn.close()

        except Exception as e:

            print(f"Failed to connect to websocket server: {e}")

    def perform_update(self, serializer):

        task = serializer.save()

        try:

            url = "http://localhost:8080/broadcast"
            parsed_url = urlparse(url)

            conn = http.client.HTTPConnection(parsed_url.hostname, parsed_url.port, timeout=2)

            payload = json.dumps({"event": "TASK UPDATED", "data": TaskSerializer(task).data})

            headers = {"Content-Type": "application/json"}

            conn.request("POST", parsed_url.path, body=payload, headers=headers)
            response = conn.getresponse()
            response.read()  # read response to complete request
            conn.close()

        except Exception as e:
            # Log the error but don’t break the update
            print(f"Failed to notify WebSocket server: {e}")

        # try:

        #     requests.post(
        #         'http://localhost:8080/broadcast',
        #         json = {
        #             'event' : 'TASK UPDATED',
        #             'data' : TaskSerializer(task).data
        #         },
        #         timeout = 2
        #     )

        # except requests.exceptions.RequestException as e:
        #     # Log the error but don’t break the update
        #     print(f"Failed to notify WebSocket server: {e}")


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class MemberViewSet(viewsets.ModelViewSet):

    queryset = Member.objects.all()
    serializer_class = MemeberSerializer
