from django.urls import path

from todo_list.views import (
    TaskListView,
    TaskCreateView,
    TagListView,
    TagUpdateView,
    TagDeleteView,
    TagCreateView,
    done,
    TaskDeleteView,
    TaskUpdateView
)

app_name = "todo_list"

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="create-task"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="delete-task"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="update-task"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("task/<int:pk>/done/", done, name="task-done")
]
