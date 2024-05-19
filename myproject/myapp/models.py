from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

#class CustomUser(AbstractUser):
#    pass

#    class Meta: #foram necessarios para nao ter o erro RuntimeError: Model class myapp.models.Agenda doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
#        app_label = 'myapp' #foram necessarios para nao ter o erro RuntimeError: Model class myapp.models.Agenda doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.

# aqui começa as configurações da tabela agenda
class Agendas(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    )
  #  class Meta: #foram necessarios para nao ter o erro RuntimeError: Model class myapp.models.Agenda doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
  #      app_label = 'myapp' #foram necessarios para nao ter o erro RuntimeError: Model class myapp.models.Agenda doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.

    professor = models.CharField(max_length=100)
    local = models.CharField(max_length=255)
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo', null=True)

    def __str__(self):
        return f"{self.professor} - {self.local} - {self.data} - {self.hora} -  {self.status}"

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='aluno')

    #class Meta:
     #   app_label = 'myapp'

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set',
        related_query_name='user',
        help_text=_('Specific permissions for this user.'),
    )