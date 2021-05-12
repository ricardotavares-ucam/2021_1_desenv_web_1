from django.contrib.auth import forms

from .models import User

# Formulário padrão para modificação de usuário
class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        # O modelo que será utilizado para criação do formulário de usuário é de acordo com nosso Users customizado
        model = User

# Formulário padrão para criação de usuário
class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        # O modelo que será utilizado para criação do formulário de usuário é de acordo com nosso Users customizado
        model = User
        fields = ('email', 'name', 'cpf', 'address', 'phone')