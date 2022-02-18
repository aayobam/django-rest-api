from django.urls import path
from .views import *



urlpatterns = [
    path('create', TodoCreateApiView.as_view(), name="create_todo"),
    path('all', TodoListApiView.as_view(), name="todo_list"),
    path('detail/<uuid:todo_id>', TodoDetailApiView.as_view(), name="todo"),
    path('update/<uuid:todo_id>', TodoUpdateApiView.as_view(), name="todo"),
    path('delete/<uuid:todo_id>', TodoDeleteApiView.as_view(), name="todo"),
]
   