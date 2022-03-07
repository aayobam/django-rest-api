import pytest
from uuid import uuid4
from apps.todos.models import Todo
from rest_framework.reverse import reverse



@pytest.mark.django_db
def test_create_todo1_view(todo1, todo2, regularuser, superuser, authenticated_superuser):
    assert len(Todo.objects.all()) == 2
    payload = {
        "title": "todo 1",
        "desc": "this first todo",
        "is_completed": False,
        "owner": superuser.id
    }
    url = reverse("create_todo")
    response = authenticated_superuser.post(url, data=payload)
    assert response.status_code == 201
    assert len(Todo.objects.all()) == 3
    assert response.data["owner"] == superuser.id
    assert response.data["owner"] != regularuser.id
    assert response.data["title"] == "todo 1"


@pytest.mark.django_db
def test_todo1_no_owner_view(todo1, todo2, superuser, authenticated_superuser):
    assert len(Todo.objects.all()) == 2
    payload = {
        "title": "todo 1",
        "desc": "the first todo",
        "is_completed": False,
    }
    url = reverse("create_todo")
    response = authenticated_superuser.post(url, data=payload)
    assert response.status_code == 400
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_todo1_list_view(todo1, todo2, superuser, authenticated_superuser):
    assert len(Todo.objects.all()) == 2
    url = reverse("todo_list")
    response = authenticated_superuser.get(url)
    assert response.status_code == 200
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_todo1_detail_view(todo1, todo2, authenticated_superuser):
    assert len(Todo.objects.all()) == 2
    url = reverse("todo_detail", kwargs={"todo_id": todo1.id})
    response = authenticated_superuser.get(url)
    assert response.status_code == 200
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_update_todo1_view(todo1, todo2, regularuser, superuser, authenticated_superuser):
    assert len(Todo.objects.all()) == 2
    payload = {
        "title": "todo 1",
        "desc": "this first todo",
        "is_completed": False,
        "owner": superuser.id
    }
    url = reverse("todo_update", kwargs={"todo_id": todo1.id})
    response = authenticated_superuser.put(url, data=payload)
    assert response.status_code == 200
    assert len(Todo.objects.all()) == 2
    assert response.data["owner"] == superuser.id
    assert response.data["owner"] != regularuser.id
    assert response.data["title"] == "todo 1"


@pytest.mark.django_db
def test_delete_todo1_view(todo1, authenticated_superuser):
    assert len(Todo.objects.all()) == 1
    url = reverse("todo_delete", kwargs={"todo_id": todo1.id})
    response = authenticated_superuser.delete(url)
    assert response.status_code == 200
    assert len(Todo.objects.all()) == 0


@pytest.mark.django_db
def test_todo1_invalid_id_view(todo1, todo2, authenticated_superuser):
    invalid_id = uuid4()
    assert len(Todo.objects.all()) == 2
    url = reverse("todo_delete", kwargs={"todo_id": invalid_id})
    response = authenticated_superuser.delete(url)
    assert response.status_code == 404
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_superuser_can_view_any_todo(todo1, todo2, authenticated_superuser):
    assert len(Todo.objects.all()) == 2
    url = reverse("todo_detail", kwargs={"todo_id": todo2.id})
    response = authenticated_superuser.get(url)
    assert response.status_code == 200
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_superuser_can_delete_any_todo(todo1, todo2, authenticated_superuser):
    assert len(Todo.objects.all()) == 2
    url = reverse("todo_delete", kwargs={"todo_id": todo2.id})
    response = authenticated_superuser.delete(url)
    assert response.status_code == 200
    assert len(Todo.objects.all()) == 1


@pytest.mark.django_db
def test_superuser_can_update_any_todo(todo1, todo2, regularuser, authenticated_superuser):
    assert len(Todo.objects.all()) == 2
    payload = {
        "title": "todo 2",
        "desc": "updating todo 2 by superuser",
        "is_completed": True,
        "owner": regularuser.id
    }
    url = reverse("todo_update", kwargs={"todo_id": todo2.id})
    response = authenticated_superuser.put(url, data=payload)
    assert response.status_code == 200
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_create_todo2_view(todo1, todo2, superuser, regularuser, authenticated_regularuser):
    assert len(Todo.objects.all()) == 2
    payload = {
        "title": "todo 2",
        "desc": "the second todo",
        "is_completed": False,
        "owner": regularuser.id
    }
    url = reverse("create_todo")
    response = authenticated_regularuser.post(url, data=payload)
    assert response.status_code == 201
    assert len(Todo.objects.all()) == 3
    assert response.data["owner"] == regularuser.id
    assert response.data["owner"] != superuser.id
    assert response.data["title"] == "todo 2"


@pytest.mark.django_db
def test_create_todo2_no_owner_view(todo1, todo2, authenticated_regularuser):
    assert len(Todo.objects.all()) == 2
    payload = {
        "title": "todo 2",
        "desc": "the second todo",
        "is_completed": False,
    }
    url = reverse("create_todo")
    response = authenticated_regularuser.post(url, data=payload)
    assert response.status_code == 400
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_todo2_list_view(todo1, todo2, superuser, authenticated_regularuser):
    assert len(Todo.objects.all()) == 2
    url = reverse("todo_list")
    response = authenticated_regularuser.get(url)
    assert response.status_code == 200
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_todo2_detail_view(todo1, todo2, authenticated_regularuser):
    assert len(Todo.objects.all()) == 2
    url = reverse("todo_detail", kwargs={"todo_id": todo2.id})
    response = authenticated_regularuser.get(url)
    assert response.status_code == 200
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_update_todo2_view(todo1, todo2, regularuser, authenticated_regularuser):
    assert len(Todo.objects.all()) == 2
    payload = {
        "title": "todo 2",
        "desc": "updating the second todo",
        "is_completed": False,
        "owner": regularuser.id
    }
    url = reverse("todo_update", kwargs={"todo_id": todo2.id})
    response = authenticated_regularuser.put(url, data=payload)
    assert response.status_code == 200
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_delete_todo2_view(todo1, todo2, authenticated_regularuser):
    assert len(Todo.objects.all()) == 2
    url = reverse("todo_delete", kwargs={"todo_id": todo2.id})
    response = authenticated_regularuser.delete(url)
    assert response.status_code == 200
    assert len(Todo.objects.all()) == 1


@pytest.mark.django_db
def test_todo2_invalid_id_view(todo1, todo2, authenticated_regularuser):
    assert len(Todo.objects.all()) == 2
    invalid_id = uuid4()
    url = reverse("todo_delete", kwargs={"todo_id": invalid_id})
    response = authenticated_regularuser.delete(url)
    assert response.status_code == 404
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_regularuser_cant_fetch_others_todo_view(todo1, todo2, authenticated_regularuser):
    assert len(Todo.objects.all()) == 2
    url = reverse("todo_detail", kwargs={"todo_id": todo1.id})
    response = authenticated_regularuser.get(url)
    assert response.status_code == 401
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_regularuser_cant_delete_others_todo_view(todo1, todo2, authenticated_regularuser):
    assert len(Todo.objects.all()) == 2
    url = reverse("todo_delete", kwargs={"todo_id": todo1.id})
    response = authenticated_regularuser.delete(url)
    assert response.status_code == 401
    assert len(Todo.objects.all()) == 2


@pytest.mark.django_db
def test_regularuser_cant_update_others_todo_view(todo1, todo2, superuser, authenticated_regularuser):
    assert len(Todo.objects.all()) == 2
    payload = {
        "title": "todo 1",
        "desc": "this first todo",
        "is_completed": False,
        "owner": superuser.id
    }
    url = reverse("todo_update", kwargs={"todo_id": todo1.id})
    response = authenticated_regularuser.put(url, data=payload)
    assert response.status_code == 401
    assert len(Todo.objects.all()) == 2
