from rest_framework import serializers

from .models import Comment, Project, Task


class ProjectSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:

        model = Project
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:

        model = Task
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:

        model = Comment
        fields = "__all__"
