from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import pandas as pd
from sklearn import linear_model
from .forms import data
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

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
            return redirect("dashboard")
        messages.error(request, "Unsuccessful account creation. Invalid Information.")
    form = NewUserForm()
    return render(request = request, template_name='create_account.html', context={"register_form":form})
    #return render(request, 'create_account.html')
    #return HttpResponse("this is the create account page")

def dashboard(request):
    return render(request, 'dashboard.html')
    #return HttpResponse("this is the dashboard")

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})
    #return render(request, 'login.html')
    #return HttpResponse("this is the login page")

def prediction(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = data(request.POST) 
        # request.Files
        if form.is_valid():
            array = []
            avgTemp = form.cleaned_data.get('avgTemp')
            rainfall = form.cleaned_data.get('rainfall')
            # Requesting File
            # file = request.FILES['training']
            # contents = file.read().decode('utf-8')
            # reader = csv.reader(contents.splitlines())
            # dataa = list(reader)
            training = pd.read_csv('/Users/viniparzanini/Downloads/3rd_Year_Project-main/Django-Project/prediction/home/static/training.csv')
            
            # Multiple Linear Regression Algorithm to predict power usage in kWh using Average Temperature and Rainfall
            # Setting Independant Values to X and Dependant values to y
            # X = [[row['Avg Temp (°C)','Rainfall (mm)'] for row in dataa]]
            # y = [[row['Usage(kWh)'] for row in dataa]]
            x = training[['Avg Temp (°C)','Rainfall (mm)', ]]
            y = training['Usage(kWh)']

            # Creating Linear Regression Object
            regr = linear_model.LinearRegression()

            # Calling fit() method which takes independent and dependent values as parameters and fills the regression object with data that describes the relationship
            regr.fit(x,y)

            # Prediction of power usage in first row using Average temp and Rainfall
            predictPower = regr.predict([[avgTemp, rainfall]])

            array.append(predictPower)

            # Multiple Linear Regression Algorithm to predict water usage in L using Average Temperature and Rainfall

            # Setting Independant Values to X and Dependant values to y
            # X = [[row['Avg Temp (°C)','Rainfall (mm)'] for row in dataa]]
            # y = [[row['Usage(L)'] for row in dataa]]
            x = training[['Avg Temp (°C)','Rainfall (mm)', ]]
            y = training['Usage(L)']

            # Creating Linear Regression Object
            regr = linear_model.LinearRegression()

            # Calling fit() method which takes independent and dependent values as parameters and fills the regression object with data that describes the relationship
            regr.fit(x,y)
            # Prediction of power usage in first row using Average temp and Rainfall
            predictWater = regr.predict([[avgTemp, rainfall]])

            array.append(predictWater)
            # Returning Water Usage Prediction
            # return HttpResponse(array, status=200)
            # return HttpResponse(redirect, predictWater, status=200)
            # return JsonResponse({'message': 'Success'}, status=200)
            # result = f"predictPower: {predictPower}, predictWater: {predictWater}"
            return render(request, 'prediction.html', {'form': form, 'predictPower': predictPower, 'predictWater': predictWater})
    else:
        form = data()
    return render(request, 'prediction.html', {'form': form})
    #return HttpResponse("this is the prediction page")

def graph(request):
    # Read the data from the CSV file
    with open('/Users/viniparzanini/Downloads/3rd_Year_Project-main/Django-Project/prediction/home/static/training.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        x_column_index = 0
        y_column_index = 4
        x = []
        y = []
        for row in reader:
            x.append(row[x_column_index])
            y.append(row[y_column_index])
    
    # Generate the chart using Matplotlib
    plt.plot(x, y)
    plt.savefig("/Users/viniparzanini/Downloads/3rd_Year_Project-main/Django-Project/prediction/home/static/data.png") 

    # Render the HTML template with the chart
    return render(request, 'graph.html')