from django.shortcuts import render, redirect, HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import pandas as pd
from sklearn import linear_model
from .forms import data
import csv

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
        if form.is_valid():
            avgTemp = form.cleaned_data.get('avgTemp')
            rainfall = form.cleaned_data.get('rainfall')
            training = pd.read_csv('C:\Django-Project\prediction\home\static/training.csv')
            
            # Multiple Linear Regression Algorithm to predict power usage in kWh using Average Temperature and Rainfall
            # Setting Independant Values to X and Dependant values to y
            X = training[['Avg Temp (°C)','Rainfall (mm)', ]]
            y = training['Usage(kWh)']

            # Creating Linear Regression Object
            regr = linear_model.LinearRegression()

            # Calling fit() method which takes independent and dependent values as parameters and fills the regression object with data that describes the relationship
            regr.fit(X,y)

            # Prediction of power usage in first row using Average temp and Rainfall
            predictPower = regr.predict([[avgTemp, rainfall]])


            # Multiple Linear Regression Algorithm to predict water usage in L using Average Temperature and Rainfall

            # Setting Independant Values to X and Dependant values to y
            X = training[['Avg Temp (°C)','Rainfall (mm)', ]]
            y = training['Usage(L)']

            # Creating Linear Regression Object
            regr = linear_model.LinearRegression()

            # Calling fit() method which takes independent and dependent values as parameters and fills the regression object with data that describes the relationship
            regr.fit(X,y)
            # Prediction of power usage in first row using Average temp and Rainfall
            predictWater = regr.predict([[avgTemp, rainfall]])

            # Returning Water Usage Prediction
            return HttpResponse(request, predictPower, predictWater)

    else:
        return render(request, 'prediction.html')
        #return HttpResponse("this is the prediction page")

def graph(request):
   # Read the data from the CSV file
        with open("C:\Django-Project\prediction\home\static/training.csv") as f:
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
        plt.savefig("C:\Django-Project\prediction\home\static/data.png") 

        # Render the HTML template with the chart
        return render(request, 'graph.html')