from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Si existe ?next=..., redirigir allí, si no ir a la vista principal del app 'core'
            next_url = request.GET.get('next') or request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('core:home')
    else:
        form = AuthenticationForm()
    return render(request, 'seguridad/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Usuario creado con éxito!')
            form = UserCreationForm()  # Limpia el formulario
        else:
            messages.error(request, 'No se ha creado el usuario. Verifica los datos.')
    else:
        form = UserCreationForm()
    return render(request, 'seguridad/register.html', {'form': form})

