import pytest
from apps.authentication.models import CustomUser
from apps.authentication.serializer import RegisterUserSerializer, UserSerializer
from rest_framework.reverse import reverse
from rest_framework.test import APIClient



api_client = APIClient()


@pytest.mark.django_db
def test_create_superuser_serializer():
    assert len(CustomUser.objects.all()) == 0
    payload = {
        "first_name": "test",
        "last_name": "user",
        "phone_no": "74536483538",
        "email": "testuser@gmail.com",
        "username": "testuser",
        "password": "notreal01",
        "is_active": True,
        "is_staff": True,
        "is_superuser": True
    }
    serializer = RegisterUserSerializer(data=payload)
    assert serializer.is_valid()
    assert serializer.save()
    assert len(CustomUser.objects.all()) == 1
    assert serializer.errors == {}


@pytest.mark.django_db
def test_create_regularuser_serializer():
    assert len(CustomUser.objects.all()) == 0
    payload = {
        "first_name": "test",
        "last_name": "user",
        "phone_no": "74536483538",
        "email": "testuser@gmail.com",
        "username": "testuser",
        "password": "notreal01",
        "is_active": True,
        "is_staff": False,
        "is_superuser": False
    }
    serializer = RegisterUserSerializer(data=payload)
    assert serializer.is_valid()
    assert serializer.save()
    assert len(CustomUser.objects.all()) == 1
    assert serializer.errors == {}


@pytest.mark.django_db
def test_create_user_no_email_serializer():
    assert len(CustomUser.objects.all()) == 0
    payload = {
        "first_name": "test",
        "last_name": "user",
        "phone_no": "74536483538",
        "username": "testuser",
        "password": "notreal01",
        "is_active": True,
        "is_staff": False,
        "is_superuser": False  
    }
    serializer = RegisterUserSerializer(data=payload)
    assert not serializer.is_valid()
    assert len(CustomUser.objects.all()) == 0
    assert serializer.errors != {}
