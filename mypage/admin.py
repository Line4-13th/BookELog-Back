from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# UserAdmin 커스터마이징
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'first_name', 'email', 'is_staff')
    search_fields = ('username', 'first_name', 'email')
    ordering = ('username',)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
