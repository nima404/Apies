from rest_framework import permissions


class IsTotalAdmin(permissions.BasePermission):
    message = 'Just Total Admin Have Access'

    def has_permission(self, request, view):
        if request.user.role <= 2:
            return True
        return False


class IsUsualAdmin(permissions.BasePermission):
    message = 'Just Usual Admin Have Access'

    def has_permission(self, request, view):
        if request.user.role == 3:
            return True
        return False


class IsSeller(permissions.BasePermission):
    message = 'Just Seller Have Access'

    def has_permission(self, request, view):
        if request.user.role == 4:
            return True
        return False


class IsService(permissions.BasePermission):
    message = 'Just Service Have Access'

    def has_permission(self, request, view):
        if request.user.role == 5:
            return True
        return False


class IsDistributor(permissions.BasePermission):
    message = 'Just Distributor Have Access'

    def has_permission(self, request, view):
        if request.user.role == 6:
            return True
        return False


class IsWriter(permissions.BasePermission):
    message = 'Just Writer Have Access'

    def has_permission(self, request, view):
        if request.user.role == 7:
            return True
        return False


class IsUser(permissions.BasePermission):
    message = 'Just User Have Access'

    def has_permission(self, request, view):
        if request.user.role == 8:
            return True
        return False
