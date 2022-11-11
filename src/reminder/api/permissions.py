from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserObjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        allow access to the reminders just by owner
        """
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.id == obj.id)


