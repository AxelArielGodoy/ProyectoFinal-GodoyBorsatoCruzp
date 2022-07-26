from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from .forms import MyUserCreationForm

from accounts.forms import MyUserCreationForm

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
