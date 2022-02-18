from django.shortcuts import get_object_or_404
from .serializers import *
from .models import User
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import logout






class RegisterUserApiView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenPairObtainView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        payload = request.data
        serializer = CustomTokenObtainPairSerializer(data=payload)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.validated_data
        return Response(response_data, status=status.HTTP_201_CREATED)



class UsersListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]


    def get_queryset(self):
        users_list = User.objects.all()
        return users_list

    def get(self, request, *args, **kwargs):

        """
        Fetches all users
        Only a super user or admin has the permission to view all users details
        """
        user = self.request.user
        if not user.is_superuser:
            return Response({"detail": "You are not authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = UserSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_class = [permissions.IsAuthenticated,]
    lookup_url_kwarg = "user_id"
    lookup_field = "id"

    def get(self, request, user_id):
        """
            Retrieves user details
        """
        user_id = self.request.user.id
        user_details = get_object_or_404(User, id=user_id)
        if not user_details:
            raise User.DoesNotExist("User not found")

        serializer = self.serializer_class(data=user_details)
        serializer.is_valid(raise_exception=True)
        return Response({"success":True, "data": serializer.data}, status=status.HTTP_200_OK)

    """
        Updates user details
    """
    def put(self, request, user_id):
        user_id = self.request.user.id
        user_details = get_object_or_404(User, id=user_id)
        if not user_details:
            raise User.DoesNotExist("User not found")
        
        serializer = self.serializer_class(data=user_details)
        serializer.is_valid(raise_exception=True)
        return Response({"success":True, "deta": serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request, user_id):
        user_id = self.request.user.id
        user_details = get_object_or_404(User, id=user_id)
        if not user_details:
            raise User.DoesNotExist("User not found")
        payload = {
            "data": user_details
        }
        serializer = self.serializer_class(data=payload, format="json")
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success":True, "deta": serializer.data}, status=status.HTTP_200_OK)
    
    """
        Deletes user's account
    """
    def delete(self, request, user_id):
        user_id = self.request.user.id
        user_details = get_object_or_404(User, id=user_id)
        if not user_details:
            raise User.DoesNotExist("User not found")

        user_details.delete()
        return Response({"success":True, "details": "data deleted"}, status=status.HTTP_200_OK)


class LogOutApiView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny, ]

    def logout(self, request):
        user = request.user
        logout(user)
        return Response({"message":"Logout Successful"}, status=status.HTTP_200_OK)