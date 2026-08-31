from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role
            and request.user.role.name.lower() == 'admin'
        )
class HasRole(BasePermission):
    required_role = None

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        return request.user.role.name.lower() == self.required_role


class IsInventoryManager(HasRole):
    required_role = "inventory manager"


class IsSalesManager(HasRole):
    required_role = "sales manager"


class IsSupplier(HasRole):
    required_role = "supplier"

