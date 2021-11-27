from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.models import FormFuncionario


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'Usuário ou senha inválidos!')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Login efetuado com sucesso!')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('login')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request, 'Nenhum campo pode ficar em branco!')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'Nome do usuário deve ter 6 caracteres ou mais!')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'E-mail inválido.')
        return render(request, 'accounts/cadastro.html')

    # Verifica se já existe e-mail cadastrado
    if User.objects.filter(email=email).exists():
        messages.error(request, 'Este e-mail já existe!')
        return render(request, 'accounts/cadastro.html')

    if len(senha) < 6:
        messages.error(request, 'Senha deve ter 6 caracteres ou mais!')
        return render(request, 'accounts/cadastro.html')

    if senha != senha2:
        messages.error(request, 'Senhas não conferem!')
        return render(request, 'accounts/cadastro.html')

    messages.success(request, 'Registrado com sucesso! Agora faça login.')

    user = User.objects.create_user(username=usuario, email=email, password=senha,
                                    first_name=nome, last_name=sobrenome)

    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormFuncionario()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormFuncionario(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Erro ao enviar o formulario.')
        form = FormFuncionario(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    nome = request.POST.get('nome')
    endereco = request.POST.get('endereco')

    if len(nome) < 5:
        messages.error(request, 'Nome deve ter 5 caracteres ou mais.')
        form = FormFuncionario(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    if len(endereco) < 5:
        messages.error(request, 'Endereço deve ter 5 caracteres ou mais.')
        form = FormFuncionario(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})


    form.save()
    messages.success(request, f'Funcionario {request.POST.get("nome")} salvo com sucesso!')
    return redirect('dashboard')
