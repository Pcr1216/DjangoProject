from django.shortcuts import render
from .MyForm import InputForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm
import mysql.connector as m
from django.contrib.auth.decorators import login_required

# database connectivity

mydatabase = m.connect(host="localhost", user="root", password="Bbshark@1234", database="pythondb1")
query = "insert into product(pname,price,quantity) values(%s,%s,%s)"  # must be "s"
query2="select * from product"
cursor = mydatabase.cursor()

# Create your views here.
def add_w(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "ADD.html", context)


def result(request):
    form = InputForm(request.POST)
    cursor.execute(query, [form['pname'].value(), form['price'].value(), form['quantity'].value()])
    # cursor.execute(query2)
    mydatabase.commit()
    return HttpResponse("Done")


def home(request):
    return render(request, 'home.html')


# def x(request):
#     return render(request, 'myhtml.html', products)
#
#
# def y(request):
#     products = {
#         "list": ["TV", "Laptop", "Mobile"]
#     }
#     return render(request, 'myhtml.html', products)
#
def view_w(request):
    cursor.execute(query2)
    x={'abc':cursor.fetchall()}
    #return HttpResponse(x)
    return render(request, 'myhtml.html',x)

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/welcome')  # Redirect to the home page after successful login
        else:
            return HttpResponse("Invalid entry")
    return render(request,'login.html')



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def shop(request):
    return render(request, 'shop.html')

def addCart(request):
    items = request.POST.getlist('product')
    if request.session.get("prodlist"):
        mylist = request.session.get("prodlist")
        mylist.extend(items)
        request.session['prodlist'] = mylist
    else:
        request.session['prodlist'] = items
    return render(request, 'home_s.html')

def viewCart(request):
    if request.session.get("prodlist"):
        mylist = request.session.get("prodlist")
        return render(request, 'viewCart.html', {'itemlist': mylist})
    else:
        return render(request, 'Empty.html')

def payment(request):
    # as if we receive payment here
    del request.session['prodlist']  # to kill the session
    return render(request, 'paymentc.html')

def welcome(request):
    return render(request, 'home_s.html')

def profile(request):
    username = request.user.username
    return HttpResponse(f"Logged in as: {username}")