from rest_framework.permissions import BasePermission


class IsRiderUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.role == 'rider')


class IsCustomerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.role == 'customer')
