# from django.shortcuts import render

# flake8: noqa

from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Comment, Member, Project, Task
from .serializers import CommentSerializer, MemeberSerializer, ProjectSerializer, TaskSerializer

# Generic Class based Views


class TaskListCreateView(ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


status


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


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class MemberViewSet(viewsets.ModelViewSet):

    queryset = Member.objects.all()
    serializer_class = MemeberSerializer
