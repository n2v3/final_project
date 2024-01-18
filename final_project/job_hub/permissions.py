from rest_framework.permissions import BasePermission

class MyCustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return request.user and request.user.is_superuser
        elif request.user.is_staff:
            # Staff can perform all actions except DELETE
            return request.method != 'DELETE'
        else:
            # Non-staff users can only perform GET
            return request.method == 'GET'

class ReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        # Allow GET requests for anyone
        return request.method == 'GET'

