from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login

def login(request):
    if request.method == 'POST':
        form_login = AuthenticationForm(request, data=request.POST)
        
        if form_login.is_valid():
            username= form_login.cleaned_data.get('username')
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
