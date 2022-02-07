from django.urls import path
from .views import TodoApiView, TodoDetailApiView



urlpatterns = [
    path('', TodoApiView.as_view(), name="create-todo"),
    path('<str:id>', TodoDetailApiView.as_view(), name="todo-detail"),

]
   