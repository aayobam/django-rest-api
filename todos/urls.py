from django.urls import path
from .views import TodoApiView, TodoDetailApiView



urlpatterns = [
    path('all', TodoApiView.as_view(), name="create-todo"),
    path('<uuid:todo_id>', TodoDetailApiView.as_view(), name="todo-detail"),
]
   