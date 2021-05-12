from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Como estamos criando um usuário diferente do padrão do Django temos que criar um gerenciador para este usuário
class UsersManager(BaseUserManager):

    #Sobrescrevendo o método da BaseUserManager
	def create_user(self, email, name, cpf, address, phone, password=None):
		if not email:
			raise ValueError('Favor inserir seu e-mail')
		if not name:
			raise ValueError('Favor inserir seu nome')
		if not cpf:
			raise ValueError('Favor inserir seu CPF')
		if not address:
			raise ValueError('Favor inserir seu Endereço')
		if not phone:
			raise ValueError('Favor inserir seu Telefone')
		
		user = self.model(
			# normaliza o email colando todas as letras minusculas
			email = self.normalize_email(email),
			name = name,
			cpf = cpf,
			address = address,
			phone = phone
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

    # Sobreescrita do método create_superuser para inserção de outras variáveis
	def create_superuser(self, email, name, cpf, address, phone, password):
		user = self.create_user(
			email=self.normalize_email(email),
			name = name,
			cpf = cpf,
			address = address,
			phone = phone,
			password = password,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

# Criando um usuário modificado
class User(AbstractBaseUser):
	email = models.EmailField(verbose_name = 'E-mail', max_length = 100, unique=True)
	name = models.CharField(verbose_name = 'Nome', max_length = 200, 
		null = False, blank = False)
	cpf = models.CharField(verbose_name = 'CPF', max_length = 14, 
		null = False, blank = False)
	address = models.CharField(verbose_name = 'Endereço', 
		max_length = 200, null = False, blank = False)
	phone = models.CharField(verbose_name = 'Telefone', 
		max_length = 14, null = False, blank = False)
	
	# Campos obrigatórios
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name', 'cpf', 'address', 'phone']
	
	# Adiciona o Gerenciador de conta sobreescrevendo alguns parametros do Django
	objects = UsersManager()

	def __str__(self):
		return self.cpf

	# Verifica se usuário tem permissão de admin
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Verifica se o usuário tem permissão para visualizar a aplicação
	def has_module_perms(self, app_label):
		return True


# APÓS A FINALIZAÇÃO DA CRIAÇÃO DO USUÁRIO MODIFICADO, ATUALIZE O ARQUIVO SETTINGS.PY 
# INCLUINDO AUTH_USER_MODEL
