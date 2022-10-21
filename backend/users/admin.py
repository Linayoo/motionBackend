from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    readonly_fields = ('date_joined',)

    # fields shown when creating a new instance
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'username', 'password1', 'password2')
        }),
    )

    # fields when reading / updating an instance
    field_sets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last login', 'date_joined')}),
        ('Social Status', {'fields': ('following', 'followers')})
    )

    # fields which are shown when looking at a list of instances
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff')
    ordering = ('-id', 'email')
