from rest_framework.permissions import BasePermission


class Mypermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            if request.user.username == "abdul1":
                return True
        return False
