# flake8:noqa

from django.contrib import admin

from .models import Comment, Member, Project, Task

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "description", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "description")


class TaskAdmin(admin.ModelAdmin):

    list_display = ("id", "title", "description", "is_completed", "created_at", "project")
    list_filter = ("created_at", "is_completed")
    search_fields = ("title", "description", "project")


class CommentAdmin(admin.ModelAdmin):

    list_display = ("content", "created_at", "task")
    list_filter = ("content", "created_at")
    search_fields = ("content", "task")


class MembersAdmin(admin.ModelAdmin):

    list_display = ("name", "created_at", "project")
    list_filter = ("name",)
    search_fields = ("name",)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Member, MembersAdmin)
