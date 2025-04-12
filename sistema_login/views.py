from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .forms import CadastroForm, LoginForm
from .models import Usuario

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            senha = form.cleaned_data['senha']
            try:
                usuario = Usuario.objects.get(nome=nome)
                if check_password(senha, usuario.senha):
                    request.session['usuario_id'] = usuario.id
                    messages.success(request, f"Bem-vindo, {nome}!")
                    return redirect('perfil')
                else:
                    messages.error(request, "Senha incorreta.")
            except Usuario.DoesNotExist:
                messages.error(request, "Usuário não encontrado.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def perfil_view(request):
    if 'usuario_id' not in request.session:
        return redirect('login')
    usuario = Usuario.objects.get(id=request.session['usuario_id'])
    return render(request, 'perfil.html', {'usuario': usuario})

def logout_view(request):
    if 'usuario_id' in request.session:
        del request.session['usuario_id']
    return redirect('login')
