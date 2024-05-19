from django.urls import path
from .views import user_login,dados_tabela,register_user,insert_update_agenda,redirect_user,update_agenda_all,update_status,dados_sair,sobre

urlpatterns = [
    path('login_usuarios/', user_login, name='login'),
   # path('profile/', profile, name='profile'),
    path('agenda_eventos/', dados_tabela, name='dados_tabela'),
    path('cadastro_usuario/', register_user, name='register'),
    path('login_usuarios/', dados_sair, name='dados_sair'),
    path('sobre/', sobre, name='sobre'),
    path('agenda/', insert_update_agenda, name='insert_update_agenda'),
    path('redirect-user/', redirect_user, name='redirect_user'),
   # path('atualizar_agenda/<int:pk>/', update_agenda, name='update_agenda'),
    path('atualizar_agenda/', update_agenda_all, name='update_agenda_all'),
    path('atualizar_status_agenda/<int:pk>/', update_status, name='update_status'),
    #path('imagem/academialogin.jpg', update_status, name='update_status'),
]

