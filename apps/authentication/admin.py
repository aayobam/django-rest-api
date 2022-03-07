from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "username",
                    "phone_no",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                    "date_joined",
                ),
            },
        ),
    )
    form = CustomUserChangeForm
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "id",
                    "first_name",
                    "last_name",
                    "email",
                    "username",
                    "phone_no",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "password",
                    "user_permissions",
                    "date_joined",
                ),
            },
        ),
    )
    
    list_display = ("id", "first_name", "last_name", "email", "username", "phone_no", "is_active", "is_staff", "is_superuser")
    readonly_fields = ("id", "date_joined")
