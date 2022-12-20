from django.shortcuts import render, redirect, HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def home(request):
    #context = {'name': 'Eoin'}
    return render(request, 'home.html')
    #return HttpResponse("this is the home page")

def create_account(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account creation successful." )
            return redirect("main:home")
        messages.error(request, "Unsuccessful account creation. Invalid Information.")
    form = NewUserForm()
    return render(request = request, template_name='create_account.html', context={"register_form":form})
    #return render(request, 'create_account.html')
    #return HttpResponse("this is the create account page")

def dashboard(request):
    return render(request, 'dashboard.html')
    #return HttpResponse("this is the dashboard")

def login(request):
    return render(request, 'login.html')
    #return HttpResponse("this is the login page")

def prediction(request):
    return render(request, 'prediction.html')
    #return HttpResponse("this is the prediction page")

def graph(request):
    return render(request, 'graph.html')
    #return HttpResponse("this is the graph page")