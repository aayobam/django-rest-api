from xml.dom.minidom import Attr
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError



class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=120, 
        min_length=8, 
        write_only=True, 
        help_text="must not be less than 8", 
        style={'input_type':"password"},
    )
    
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

   

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def delete(self, instance, validated_data):
        for key, value in validated_data.items():
            return Attr(key, value, instance)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            return(instance, key, value)


class LogoutSerializer(serializers.Serializer):
    """
    The refresh tokens created when users signin are blacklisted after logging out
    Simple JWT blacklist option does this so the refresh tokens can't be used again
    """

    def validate(self, validated_data):
        self.token = validated_data["refresh"]
        return validated_data

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")
