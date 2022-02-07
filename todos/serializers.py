from .models import Todo
from rest_framework import serializers



class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'

    def post(self, validated_data):
        todo = Todo.objects.get_or_create(**validated_data)
        return todo

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            return(instance, key, value)
