# django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# local
from .models import CustomUser
from .custom_fieldset import FieldSets


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    """
        Adds CustomAdmin into Admin panel
    """
    list_display = (
        'uid',
        'username',
        'email',
        'is_staff',
        'is_superuser',
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')
    fieldsets = FieldSets(
        none=('uid', 'password'),
        Personal_info=('username', 'email', 'secret_code'),
        Permissions=(
            ('is_active', 'is_staff', 'is_superuser'),
            ('groups', 'user_permissions'),
        ),
        Important_dates=('last_login', 'date_joined'),
    )

    add_fieldsets = FieldSets(none=('uid', 'email', 'password1', 'password2'))

    search_fields = ('uid', 'username', 'email')
    ordering = (
        '-date_joined',
        'username',
    )
