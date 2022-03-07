import pytest
from apps.todos.models import Todo
from apps.todos.serializers import TodoSerializer


@pytest.mark.django_db
def test_todo1_serializer(superuser):
    assert len(Todo.objects.all()) == 0
    payload = {
        "title": "todo 1",
        "desc": "this first todo",
        "is_completed": False,
        "owner": superuser.id
    }
    serializer = TodoSerializer(data=payload)
    assert serializer.is_valid()
    assert serializer.save()
    assert len(Todo.objects.all()) == 1
    assert serializer.errors == {}


@pytest.mark.django_db
def test_todo1_no_owner_serializer():
    assert len(Todo.objects.all()) == 0
    payload = {
        "title": "todo 1",
        "desc": "the first todo",
        "is_completed": False,
    }
    serializer = TodoSerializer(data=payload)
    assert not serializer.is_valid()
    assert len(Todo.objects.all()) == 0
    assert serializer.errors != {}


@pytest.mark.django_db
def test_todo2_serializer(regularuser):
    assert len(Todo.objects.all()) == 0
    payload = {
        "title": "todo 2",
        "desc": "the second todo",
        "is_completed": False,
        "owner": regularuser.id
    }
    serializer = TodoSerializer(data=payload)
    assert serializer.is_valid()
    assert serializer.save()
    assert len(Todo.objects.all()) == 1
    assert serializer.errors == {}


@pytest.mark.django_db
def test_todo2_no_owner_serializer():
    assert len(Todo.objects.all()) == 0
    payload = {
        "title": "todo 2",
        "desc": "the second todo",
        "is_completed": False,
    }
    serializer = TodoSerializer(data=payload)
    assert not serializer.is_valid()
    assert len(Todo.objects.all()) == 0
    assert serializer.errors != {}