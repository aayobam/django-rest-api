from rest_framework import serializers
from .models import User




class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=120, min_length=8, write_only=True, help_text="must not be less than 8")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=120, min_length=8, write_only=True, help_text="must not be less than 8")

    class Meta:
        model = User
        fields = ['email', 'password', 'token']
        read_only_fields = ['token']