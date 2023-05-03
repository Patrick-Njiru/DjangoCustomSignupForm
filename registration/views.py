from django.shortcuts import render, redirect
from .forms import UserCreationForm, SignUpForm
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'registration/home.html', {'user': ""})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            username = form['username']
            password1 = form['password1']
            password2 = form['password2']
            if password1 == password2: 
                form.save()
                new_user = authenticate(username=username, password=password1)
                if new_user is not None:
                    login(request, new_user)
                    redirect('home:html')
    
    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)

# def login(r)
