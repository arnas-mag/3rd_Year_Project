from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    #context = {'name': 'Eoin'}
    return render(request, 'home.html')
    #return HttpResponse("this is the home page")

def create_account(request):
    return render(request, 'create_account.html')
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