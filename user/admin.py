from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import Client


@admin.register(Client)
class ClientAdmin(UserAdmin):
    """ Since we have created using abstractBaseUser we need to override the UserAdmin to tel about all the fields
    and display. If i don't do add_fieldsets then email won't be included in admin registration form"""
    add_fieldsets = (
        (
            'Signup',
            {
                "fields": ("username", 'email', "password1", "password2"),
            },
        ),
    )
    list_display = ['username', 'email', ]