from django.shortcuts import render
from .MyForm import InputForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm
import mysql.connector as m
from django.contrib.auth.decorators import login_required
from .models import Product

# database connectivity

mydatabase = m.connect(host="localhost", user="root", password="mysql@123", database="pythondb1")
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
        print(user.get_username)
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
    if request.method == 'POST':
        products = request.POST.getlist('product')
        quantities = request.POST.getlist('quantity')  # Get quantities submitted in the form
        for product, quantity in zip(products, quantities):
            # Create a new Product instance with the submitted quantity and save it to the database
            product_obj = Product(prodname=product, quantity=quantity)
            product_obj.save()
        return render(request, 'home_s.html')  # Redirect to the home page after adding products
    else:
        return render(request, 'home_s.html')

def viewCart(request):
    print("hello")
    if request.method == 'GET':
        # Query only the prodname and quantity fields
        prod_list = Product.objects.values('prodname', 'quantity')
        print(prod_list)
        context = {'productlist': prod_list}  # Correct the key to match the template
        print(context)
        return render(request, 'viewCart.html', context=context)  # Correct template name
    else:
        return render(request, 'Empty.html')

def payment(request):
    # as if we receive payment here
    Product.objects.all().delete()
    return render(request, 'paymentc.html')

def welcome(request):
    return render(request, 'home_s.html')

def profile(request):
    username = request.user.username
    return HttpResponse(f"Logged in as: {username}")