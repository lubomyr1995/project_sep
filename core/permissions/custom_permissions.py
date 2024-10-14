from django.contrib.auth import get_user_model

from rest_framework.permissions import BasePermission

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class IsAdminOrWriteOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        user: User = request.user
        return user.is_staff
