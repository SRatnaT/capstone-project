# from django.shortcuts import render

# flake8: noqa

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Comment, Member, Project, Task
from .serializers import CommentSerializer, MemeberSerializer, ProjectSerializer, TaskSerializer

# Create your views here.


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
