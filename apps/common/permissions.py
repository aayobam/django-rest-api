
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to view or edit it.
    Assumes the model instance has an `owner` attribute.

    A superuser is allowed all crude operations
    """


    def has_object_permission(self, request, view, obj):
      
        if request.user.is_superuser:
            return True

        return obj == request.user or request.user.is_superuser


class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow superuser to read data
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_superuser)
        return False


class HasTodoPermissionOrReadOnly(permissions.BasePermission):
    

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.owner == request.user:
            return True

        return False

class CanDeleteUserAccount(permissions.BasePermission):

    """
    Object-level permission to only allow owners of an object to view 
    or delete it. Assumes the model instance has an `owner` attribute.
    A superuser is allowed all permissions.
    """

    def has_object_permission(self, request, view, obj):
        
        if request.user.is_superuser:
           return True
        
        if obj == request.user:
            return True
            
        return False
