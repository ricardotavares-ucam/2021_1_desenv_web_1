from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

class UsersAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('name', 'cpf', 'address', 'phone',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'cpf', 'address', 'phone',)}),
    )
    list_display = ('id','email', 'name', 'address', 'phone')
    list_filter = ('is_admin', 'is_active', 'is_superuser')
    search_fields = ('email', 'name', 'cpf')
    ordering = ('email','name')

    filter_horizontal = ()
admin.site.register(User, UsersAdmin)