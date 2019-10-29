from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # Get values from form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check password
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'user name is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    auth.login(request, user)
                    messages.success(request, 'you are logged in')
                    return redirect('homepage')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Welcome back")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    else:   
        return render(request, "login.html")

def logout(request): 
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "logged out successfully")
        return redirect('homepage')

def frequent(request):
    return render(request, 'frequent.html')

def single(request):
    return render(request, 'single.html')

def dashboard(request):
    return render(request, 'dashboard.html')