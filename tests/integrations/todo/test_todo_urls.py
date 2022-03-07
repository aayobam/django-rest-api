import pytest
from django.urls import resolve
from rest_framework.reverse import reverse
from apps.todos.views import (
    TodoCreateApiView,
    TodoListApiView,
    TodoDetailApiView,
    TodoUpdateApiView,
    TodoDeleteApiView
)



@pytest.mark.django_db
def test_create_todo_url_is_resolved():
    url = reverse("create_todo")
    assert resolve(url).func.view_class == TodoCreateApiView


@pytest.mark.django_db
def test_todo_list_url_is_resolved():
    url = reverse("todo_list")
    assert resolve(url).func.view_class == TodoListApiView


@pytest.mark.django_db
def test_todo_detail_url_is_resolved(todo2):
    url = reverse("todo_detail", kwargs={"todo_id": todo2.id})
    assert resolve(url).func.view_class ==  TodoDetailApiView


@pytest.mark.django_db
def test_update_todo_url_is_resolved(todo2):
    url = reverse("todo_update", kwargs={"todo_id": todo2.id})
    assert resolve(url).func.view_class ==  TodoUpdateApiView


@pytest.mark.django_db
def test_delete_todo_url_is_resolved(todo2):
    url = reverse("todo_delete", kwargs={"todo_id": todo2.id})
    assert resolve(url).func.view_class ==  TodoDeleteApiView