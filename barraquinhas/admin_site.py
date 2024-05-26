from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

class CustomAdminSite(AdminSite):
    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff

    def has_view_permission(self, request, obj=None):
        if obj in [User, Group] or (hasattr(obj, '_meta') and obj._meta.model in [User, Group]):
            return False
        return super().has_view_permission(request, obj)

custom_admin_site = CustomAdminSite(name='custom_admin')
custom_admin_site.register(User, UserAdmin)
custom_admin_site.register(Group, GroupAdmin)