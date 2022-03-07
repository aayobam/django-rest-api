import pytest
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from apps.authentication.models import CustomUser
from apps.todos.models import Todo



@pytest.fixture(scope="function")
def superuser():
    return CustomUser.objects.create_superuser(
        first_name="super",
        last_name="user",
        phone_no= "03647394756",
        email="superuser@gmail.com",
        username= "superuser",
        password= "notreal01",
        is_active=True,
        is_staff=True,
        is_superuser=True
    )


@pytest.fixture(scope="function")
def authenticated_superuser(superuser):
    api_client = APIClient()
    payload = {
        "email": "superuser@gmail.com",
        "password": "notreal01"
    }
    url = reverse("access_token")
    response = api_client.post(url, data=payload)
    assert response.status_code == 201
    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client


@pytest.fixture(scope="function")
def regularuser():
    return CustomUser.objects.create_user(
        first_name="regular",
        last_name="user",
        phone_no= "47304638404",
        email="regularuser@gmail.com",
        username= "regularuserr",
        password= "notreal01",
        is_active=True,
        is_staff=False,
        is_superuser=False
    )


@pytest.fixture(scope="function")
def authenticated_regularuser(regularuser):
    api_client = APIClient()
    payload = {
        "email": "regularuser@gmail.com",
        "password": "notreal01"
    }
    url = reverse("access_token")
    response = api_client.post(url, data=payload)
    assert response.status_code == 201
    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client


@pytest.fixture(scope="function")
def todo1(superuser):
    return Todo.objects.create(
        title = "todo 1",
        desc="the first todo",
        is_completed=True,
        owner=superuser
    )

@pytest.fixture(scope="function")
def todo2(regularuser):
    return Todo.objects.create(
        title = "todo 2",
        desc="the second todo",
        is_completed=True,
        owner=regularuser
    )