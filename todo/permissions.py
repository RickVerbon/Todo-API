from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only access for all requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user making the request is the owner of the Todo object
        return obj.user == request.user
