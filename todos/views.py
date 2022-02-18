from django.shortcuts import get_object_or_404
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status, filters
from rest_framework.response import Response
from.pagination import CustomPageNUmberPagination
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics




class TodoCreateApiView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_class = [IsAuthenticated,]
    pagination_class = CustomPageNUmberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'title', 'is_completed']
    search_fields = ['id', 'title', 'is_completed']
    ordering_fields = ['id', 'title', 'is_completed']

    def get_queryset(self):
        user = self.request.user
        todo_list = Todo.objects.filter(owner=user)
        if not user or user.is_authenticated:
            return Response({"message": "Login is required"}, status=status.HTTP_401_UNAUTHORIZED)
        return todo_list

    def perform_create(self, request):
        user = self.request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=user)
            return Response({"success":True, "data":serializer.data}, status=status.HTTP_201_CREATED)
        Response({"success":False, "detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def perform_get(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoListApiView(generics.RetrieveAPIView):
    serializer_class = TodoSerializer
    permission_class = [IsAuthenticated,]
    pagination_class = CustomPageNUmberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'title', 'is_completed']
    search_fields = ['id', 'title', 'is_completed']
    ordering_fields = ['id', 'title', 'is_completed']

    def get_queryset(self):
        user = self.request.user
        todo_list = Todo.objects.filter(owner=user)
        return todo_list

    def get(self):
        serializer = self.serializer_class(data=self.get_queryset())
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TodoDetailApiView(generics.RetrieveAPIView):
    serializer_class = TodoSerializer
    permission_class = [IsAuthenticated,]
    lookup_field = "id"
    lookup_url_kwarg = "todo_id"

    def get_queryset(self, request):
        user = self.request.user
        todo_list = Todo.objects.filter(owner=user)
        return todo_list

    def list(self):
        serializer = self.serializer_class(data=self.get_queryset())
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TodoUpdateApiView(generics.RetrieveUpdateAPIView):
    serializer_class = TodoSerializer
    permission_class = [IsAuthenticated,]
    lookup_field = "id"
    lookup_url_kwarg = "todo_id"

    def get_queryset(self, todo_id):
        user = self.request.user
        todo_list = get_object_or_404(Todo, id=todo_id).filter(owner=user)
        return todo_list

    def put(self):
        user = self.request.user
        serializer = self.serializer_class(data=self.get_queryset())
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self):
        user = self.request.user
        serializer = self.serializer_class(data=self.get_queryset())
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TodoDeleteApiView(generics.RetrieveDestroyAPIView):
    serializer_class = TodoSerializer
    permission_class = [IsAuthenticated,]
    lookup_field = "id"

    def get_queryset(self, request, todo_id):
        user = self.request.user
        todo = get_object_or_404(Todo, id=todo_id)
        if todo.owner == user or user.is_superuser:
            todo.delete()
            return Response({"success":True}, status=status.HTTP_200_OK)
        return Response({"detail":"you are not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)
