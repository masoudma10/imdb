from rest_framework.permissions import BasePermission
from users.models import User


class UserPermissions(BasePermission):
    """
    permission for admin users
    """
    def has_permission(self, request, view):
        user = User.objects.get(email=request.user.email)
        if user.is_admin == True:
            return True
        else:
            return False





