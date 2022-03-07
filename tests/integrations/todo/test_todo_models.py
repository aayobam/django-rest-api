import pytest
from apps.todos.models import Todo


@pytest.mark.django_db
def test_todo_model(todo1, todo2):
    assert isinstance(todo1, Todo)
    assert isinstance(todo2, Todo)
    assert todo1 != todo2