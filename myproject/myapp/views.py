from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']

            # Autenticar o usuário com base no username, password e user_type
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Verificar se o user_type corresponde ao esperado
                if user.user_type == user_type:
                    login(request, user)
                    if user_type == 'aluno':
                        return redirect('dados_tabela')
                    elif user_type == 'professor':
                        return redirect('insert_update_agenda')
                    #return redirect('dados_tabela')
                    
                else:
                    error_message = "Tipo de usuário incorreto."
            else:
                error_message = "Nome de usuário ou senha incorretos."

            return render(request, 'login_usuario.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()

    return render(request, 'login_usuario.html', {'form': form})

#codigo para mostrar o login os dados do usuario no bando de dados apos login

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


 
 #configuração tabela de agenda
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Agendas

@login_required
def dados_tabela(request):
    # Recupere os dados da tabela
    dados = Agendas.objects.all()
    return render(request, 'agenda_eventos.html', {'dados': dados})

def dados_sair(request):
    # Recupere os dados da tabela
    #dados = Agendas.objects.all()
    return render(request, 'login_usuario.html')

def sobre(request):
    # Recupere os dados da tabela
    #dados = Agendas.objects.all()
    return render(request, 'sobre.html')

# tela de registro

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'cadastro_usuario.html', {'form': form})

# poder de insert
from django.shortcuts import render, redirect
from .forms import AgendaForm

def insert_update_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dados_tabela')
    else:
        form = AgendaForm()
    return render(request, 'agenda.html', {'form': form})

# poder de marcar inativo ou ativo
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser

@login_required
def redirect_user(request):
    user_type = request.user.user_type
    if user_type == 'aluno':
        return redirect('dados_tabela')
    elif user_type == 'professor':
        return redirect('insert_update_agenda')
    
from django.shortcuts import render
from .models import Agendas

def update_agenda_all(request):
    # Recupera todos os registros da tabela de agenda
    agendas = Agendas.objects.all()

    # Retorna a renderização da página de atualização para todos os registros
    return render(request, 'atualizar_agenda_all.html', {'agendas': agendas})


from django.shortcuts import get_object_or_404, redirect, render
from .models import Agendas

def update_status(request, pk):
    agenda = get_object_or_404(Agendas, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        print(f"Status recebido: {status}")  # Para depurar
        agenda.status = status
        agenda.save()
        return redirect('update_agenda_all')  

    return render(request, 'atualizar_status_agenda.html', {'agenda': agenda})
