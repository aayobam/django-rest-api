from tabnanny import verbose
from django.db import models
from apps.authentication.models import CustomUser
from uuid import uuid4




class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
        ordering = ('-created_at',)

    def __str__(self):
        return self.title