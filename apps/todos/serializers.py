from .models import Todo
from rest_framework import serializers



class TodoSerializer(serializers.ModelSerializer):
    title = serializers.CharField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'desc', 'is_completed', 'owner']

    def post(self, validated_data):
        todo = Todo.objects.create(**validated_data)
        return todo

    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance