from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from.pagination import CustomPageNUmberPagination
from rest_framework import status, filters, generics
from apps.common.permissions import (IsSuperUserOrReadOnly, IsOwnerOrReadOnly, HasTodoPermissionOrReadOnly)
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend



class TodoCreateApiView(generics.CreateAPIView):
    """
    Users must be authenticated to create todo(s)
    """
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_class = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = CustomPageNUmberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    def perform_create(self, request):
        user = self.request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoListApiView(generics.ListAPIView):
    """
    Each user can fetch his/her todo(s) but can't view other
    users todo list.Only the superuser can fetch all todo(s).
    """
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_class = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = CustomPageNUmberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title']
    search_fields = ['title']
    ordering_fields = ['title']

    def get(self, request):
        user = request.user or request.user.is_superuser
        todo = Todo.objects.filter(owner=user)
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TodoDetailApiView(generics.RetrieveAPIView):
    """
    Each user can fetch his/her todo(s) but can't view other 
    users todo details. Only the superuser can fetch all todo(s).
    """
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_class = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "id"
    lookup_url_kwarg = "todo_id"

    def get(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, id=kwargs["todo_id"])
        if todo.owner == request.user or request.user.is_superuser:
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail":"you are not allowed to view this detail"}, status=status.HTTP_401_UNAUTHORIZED)


class TodoUpdateApiView(generics.RetrieveUpdateAPIView):
    """
    Each user can edit/update his/her todo detail but can't edit/update other
    users todo details. Only the superuser can update all users todo details.
    """
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_class = [IsAuthenticated, HasTodoPermissionOrReadOnly]
    lookup_field = "id"
    lookup_url_kwarg = "todo_id"

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response_data = response.data
        return Response(response_data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, pk=kwargs["todo_id"])
        if todo.owner == request.user or request.user.is_superuser:
            response = super().patch(request, *args, **kwargs)
            response_data = response.data
            return Response(response_data, status=status.HTTP_200_OK)
        return Response({"detail":"you are not allowed to edit todo"}, status=status.HTTP_401_UNAUTHORIZED)


class TodoDeleteApiView(generics.DestroyAPIView):
    """
    Each user can delete his/her todo(s) but can't delete other
    users todo(s). Only the superuser can delete all users todo(s).
    """
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_class = [IsAuthenticated, HasTodoPermissionOrReadOnly]
    lookup_field = "id"
    lookup_url_kwarg = "todo_id"

    def delete(self, request, *args, **kwargs):
        todo = get_object_or_404(Todo, id=kwargs["todo_id"])
        if todo.owner == request.user or request.user.is_superuser:
            todo.delete()
            return Response({"detail":"todo deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"detail":"you are not authorized delete todo"}, status=status.HTTP_401_UNAUTHORIZED)
