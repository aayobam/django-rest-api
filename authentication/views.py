from .serializers import *
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView




class AuthUserApiview(GenericAPIView):

    permission_classes = [permissions.IsAuthenticated,]

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response({"user":serializer.data}, status=status.HTTP_200_OK)


class RegisterApiView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message":"Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)
            
