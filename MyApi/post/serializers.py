from rest_framework import serializers
from .models import Post, PostRate


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'post_title', 'post_body', 'rates']
        depth = 1


class PostRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRate
        fields = ['id', 'likes', 'dislikes']
