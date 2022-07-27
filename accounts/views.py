from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView


from accounts.models import MasDatosUsuarios
from .forms import MyUserCreationForm, MyUserEditForm
from django.contrib.auth.decorators import login_required



def login(request):
    if request.method == 'POST':
        form_login = AuthenticationForm(request, data=request.POST)
        
        if form_login.is_valid():
            username = form_login.cleaned_data.get('username')
            password= form_login.cleaned_data.get('password')
            
            user=authenticate(username=username, password=password)
        
            if user is not None:
                django_login (request, user)
                return render (request, 'inicio.html', {})
            else:
                return render(request, 'accounts/login.html', {'form_login': form_login})
        else:
            return render(request, 'accounts/login.html', {'form_login': form_login})
            
    
    form_login = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form_login': form_login})


def new_account (request):
    if request.method == 'POST':
        form_new_account = MyUserCreationForm(request.POST)
        if form_new_account.is_valid():
            form_new_account.save()
            return render (request, 'inicio.html', {})
        else:
            return render(request, 'accounts/new_account.html', {'form_new_account': form_new_account} )
    
    form_new_account=MyUserCreationForm()
    return render (request, 'accounts/new_account.html', {'form': form_new_account})

@login_required
def perfil(request):
    return render (request, 'accounts/perfil.html')

@login_required

def editar_perfil(request):
    
    user = request.user
    mas_datos_usuarios, _ = MasDatosUsuarios.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form_edit= MyUserEditForm(request.POST, request.FILES)
        if form_edit.is_valid():
            data = form_edit.cleaned_data
            user.first_name = data.get('first_name') if data.get('first_name') else user.first_name
            user.last_name = data.get('last_name') if data.get('last_name') else user.last_name
            user.email = data.get('email') if data.get('email') else user.email
            mas_datos_usuarios.avatar = data.get('avatar') if data.get('avatar') else mas_datos_usuarios.avatar
            
            #if data.get('password1') and data.get('password1') == data.get('password2'):
             #   user.set_password(data.get('password1'))
            
            mas_datos_usuarios.save()
            user.save()
            
            return redirect('perfil')
        
        else:
            return render(request, 'accounts/editar_perfil.html', {'form_edit':form_edit} )    
            
    
    form_edit = MyUserEditForm(
        initial={
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'avatar': mas_datos_usuarios.avatar,
        }
    )
             
    return render (request, 'accounts/editar_perfil.html', {'form_edit':form_edit})

class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/cambiar_contra.html'
    succes_url = '/accounts/perfil'
    