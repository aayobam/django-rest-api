from django.contrib import admin
from .models import *

@admin.register(Todo)
class AdminTodo(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc', 'is_completed', 'owner', 'created_at', 'updated_at')
