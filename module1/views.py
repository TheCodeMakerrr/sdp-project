from datetime import timedelta  # Import timedelta from datetime module

from django.contrib.sites import requests

from .forms import IntegerDateForm  # Import your form
import random
import string
from .views import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Register


def hi(request):
        return render(request, 'hi.html')
def newhomepage(request):
        return render(request,'newhomepage.html')
def travelpackage(request):
        return render(request, 'travelpackage.html')
   #     return HttpResponse("<h1><center style='color:blue'>Welcome to ttm home page</center></h1>")
def print_to_web(request):
        return render(request,'print_to_console.html')


def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST.get('t1')
        print(f'User input: {user_input}')
    return HttpResponse('Form is submitted')

def getdate1(request):
    return render(request,'get_date.html')

def get_date(request):
    if request.method == "POST":
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']  # Fix variable name here
            updated_date = date_value + timedelta(days=integer_value)
            return render(request, 'get_date.html', {'updated_date': updated_date})
    else:
        form = IntegerDateForm()
    return render(request, 'get_date.html', {'form': form})

# def random1(request):
#     return render(request,"random.html")
def random12(request):
    context = {}

    if request.method == 'POST':
        input1 = request.POST.get('input3')
        if input1:
            try:
                input2 = int(input1)
                if input2 > 0:
                    result_str = ''.join(random.sample(string.digits, min(input2, 12)))
                    context = {'result_str': result_str}
                else:
                    context = {'error_message': 'Please enter a positive integer.'}
            except ValueError:
                context = {'error_message': 'Please enter a valid integer.'}
        else:
            context = {'error_message': 'Input field is empty.'}

    return render(request, "random12.html", context)
def specificlocationtime(request):
    return render(request, "specificlocationtime.html")

def registerloginfunction(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            message1="Eamil already registered. Choose a different email"
            return render(request,'myregisterpage.html',{'message':message1})
        Register.objects.create(name=name,email=email,password=password)
        return redirect('newhomepage')
    return render(request,'database.html')

import matplotlib.pyplot as plt
import numpy as np

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})


def carousel(request):
    return render(request, 'carousel.html')


from django.shortcuts import render

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST.get('place', '').strip()

        if not place:
            error_message = 'Please enter a valid city.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})

        API_KEY = '65304f578a17f3b6dc69ec6a7806726f'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1 = round(temperature - 273.15, 2)
            return render(request, 'weatherappinput.html', {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})

    return render(request, 'weatherappinput.html')  # Add a default rendering for GET requests





def contactus(request):
    return render(request,'contact.html')

def contactmail(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        comment=request.POST['comment']
        tosend=comment + '---------------- This is just the contact page'
        data=contactus(firstname=firstname, lastname=lastname, email=email, comment=comment)
        data.save()
        # send_mail(
        #     'Thankyou for contacting',
        #     tosend,
        #     'just900@gmail.com',
        #     [email],
        #     fail_silently=False,
        # )
        return HttpResponse("<h1>Mail Sent</h1>")
    else:
        return HttpResponse("<h1>error</h1>")

def signup(request):
    return render(request, 'signup.html')
def login(request):
    return render(request, 'login.html')

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages

# Other imports remain the same

def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'newhomepage.html')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.success(request, 'Account created successfully!')
                return render(request, 'login.html')
        else:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')

