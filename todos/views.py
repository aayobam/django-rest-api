from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status, filters
from rest_framework.response import Response
from.pagination import CustomPageNUmberPagination
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView




class TodoApiView(ListCreateAPIView):
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
        if not user.is_authenticated:
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
        user = self.request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=user)
            return Response({"success":True, "data":serializer.data}, status=status.HTTP_200_OK)
        Response({"success":False, "detail":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_class = [IsAuthenticated,]
    lookup_field = "id"

    def get_queryset(self, request):
        user = self.request.user
        todo_list = Todo.objects.filter(owner=user)
        return todo_list
