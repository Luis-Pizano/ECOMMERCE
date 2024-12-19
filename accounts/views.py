from django.shortcuts import render, redirect # type: ignore
from .models import Account
from accounts.forms import RegistartionForm # type: ignore
from django.contrib import auth, messages # type: ignore

def register(request):
    if request.method == "POST":
        form = RegistartionForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request,'se ha guardado con exito la información')
    form = RegistartionForm()
        
    return render(request, 'register.html', context= {'form':form})


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
