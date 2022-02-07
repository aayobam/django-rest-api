from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from .models import Todo
from uuid import uuid4




class TestTodo(APITestCase):

    client = APIClient()
    todo_counts = Todo.objects.all().count()

    def authenticate(self):
        register_url = reverse("register")
        register_payload = {
            "email": "testcase@gmail.com",
            "username": "testcase",
            "password": "password@01",
        }
        response = self.client.post(url=register_url, data=register_payload)
        self.assertEquals(response.status_code, 201)

        login_url = reverse("login")
        login_payload = {
            "email": "testcase@gmail.com",
            "username": "testcase",
            "password": "password@01",
        }
        response = self.client.post(url=login_url, data=login_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        token = response.data["token"]
        print("THE USER TOKEN = ", token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_should_not_create_todo(self):
        url = reverse("create-todo")
        payload = {
            "title": "first todo",
            "desc": "this is the first todo",
            "is_completed": False,
        }
        response = self.client.post(url = url, data = payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_user_create_todo(self):
        self.authenticate()
        url = reverse("create-todo")
        payload = {
            "title": "first todo",
            "desc": "this is the first todo",
            "is_completed": False,
        }
        response = self.client.post(url=url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "first todo")
        self.assertEqual(response.data["desc"], "this is the first todo")
        self.assertEqual(response.data["is_completed"], False)
        


    def test_fetch_all_todos(self):
        self.authenticate()
        url = reverse("todo-detail")
        response = self.client.get(url=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.todo_counts, self.todo_counts+1)
        self.assertIsInstance(response.data["result"], list)

    def test_fetch_todo_detail_with_valid_id(self):
        self.authenticate()
        todo_response = self.test_auth_user_create_todo()
        url = reverse("todo-detail", kwargs={"todo_id": todo_response.data["id"]})
        response = self.client.get(url=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data["result"], list)
        self.assertEqual(response.data["id"], todo_response.data["id"])

    def test_fetch_todo_detail_with_invalid_id(self):
        self.authenticate()
        generated_id = uuid4()
        url = reverse("todo-detail", kwargs={"todo_id": generated_id})
        response = self.client.get(url=url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIsInstance(response.data["result"], list)
        
    def test_update_todo_detail(self):
        self.authenticate()
        todo_response = self.test_auth_user_create_todo()
        url = reverse("todo", kwargs={"todo_id": todo_response.data["id"]})
        payload = {
            "title": "first todo update",
            "desc": "this is the first todo update",
            "is_completed": False,
        }
        response = self.client.patch(url=url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response.data["result"], list)

    def test_delete_todo_detail(self):
        self.authenticate()
        todo_response = self.test_fetch_todo_detail_with_valid_id()
        url = reverse("todo-detail", kwargs={"todo_id": todo_response.data["id"]})
        response = self.client.delete(url=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.errors, {})
        