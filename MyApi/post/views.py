from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post, PostRate
from .serializers import PostSerializer, PostRateSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        posts = Post.objects.all()
        return posts

    def create(self, request, *args, **kwargs):
        post_data = request.data
        new_rate = PostRate.objects.create(
            likes=post_data["rates"]['likes'], dislikes=post_data["rates"]['dislikes'])
        new_rate.save()

        new_post = Post.objects.create(
            post_title=post_data['post_title'], post_body=post_data["post_body"], rates=new_rate)
        new_post.save()
        serializer = PostSerializer(new_post)
        return Response(serializer.data)


class PostRateViewSet(viewsets.ModelViewSet):
    serializer_class = PostRateSerializer

    def get_queryset(self):
        postrates = PostRate.objects.all()
        return postrates
