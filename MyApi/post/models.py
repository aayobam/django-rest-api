from django.db import models


class PostRate(models.Model):
    likes = models. BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)

    def __str__(self):
        return f"Posts Rates"


class Post(models.Model):
    rates = models.OneToOneField(PostRate, on_delete=models.CASCADE, null=True)
    post_title = models.CharField(max_length=150)
    post_body = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.post_title}"
