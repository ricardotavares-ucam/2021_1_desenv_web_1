from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

class UsersAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('id','email', 'name', 'address', 'phone')
    list_filter = ('is_admin', 'is_active', 'is_superuser')
    search_fields = ('email', 'name', 'cpf')
    ordering = ('email','name')

    filter_horizontal = ()
admin.site.register(User, UsersAdmin)