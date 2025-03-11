from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout







# Create your views here.
def register(request):
      if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
          register_form.save()
          messages.success(request,("New User Created!"))
          return redirect('register')
      else:
          register_form = CustomRegistrationForm()
      return render(request, 'register.html', {'register_form': register_form})
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
          messages.error(request, ("Invalid username or password"))
        return render(request, 'login.html')

def logout(request):
    user = request.POST.get('logout')
    if user:
        logout(request) 
      
    messages.success(request,())  
    return render(request, 'logout.html')
   

      

        
        
        
        
      
    
  
  


