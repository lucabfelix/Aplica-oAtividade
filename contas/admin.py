from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserAdminCreationForm, UserAdminForm


class UserAdmin(BaseUserAdmin):

    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None, {
            'fields': ('cpf', 'username', 'name', 'email', 'telefone', 'password1', 'password2')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None, {
            'fields': ('cpf', 'username', 'name', 'email', 'telefone')
        }),
    )
    list_display = ['cpf', 'username', 'name', 'email', 'telefone', 'is_active', 'is_staff', 'date_joined']


admin.site.register(User, UserAdmin)