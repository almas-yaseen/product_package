from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login
from products.models import customuser
from django.contrib import auth
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request,'base.html')


def signin(request):
    if request.user.is_authenticated:
         return redirect('home')
    return render(request,'signin.html')


@never_cache
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        phone_number = request.POST.get('number')

        error_messages = []

        if customuser.objects.filter(username=username).exists():
            error_messages.append('Username already exists')

       
        if not password or len(password) <= 5:
            error_messages.append('Password too short')
            
        if password != confirm_password:
            error_messages.append('Password mismatch')

        if not email or '@' not in email:
            error_messages.append('Invalid email')

        if not phone_number or len(phone_number) != 10:
            error_messages.append('Invalid phone number')

        if error_messages:
            for message in error_messages:
                messages.error(request, message)
            return render(request, 'signin.html')

        user = customuser.objects.create_user(username=username, email=email, password=password, phone_number=phone_number)
        user.save()
        messages.success(request, 'Registration successful')
        return redirect('index')

    return render(request, 'signin.html')
 
 
@never_cache
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        print("asdlkjnasdkjlnajskld")
        username = request.POST['name']
        password = request.POST['password']
        print("email ajsdasdasdasd                  ->", username)
        print("password",password)
        
        user = authenticate(username=username, password=password)
        print("Authenticated user:", user)
        
        if user is not None:
            print("user not noneasdafadfssdafffffffffffasdff")
            auth.login(request,user)
            messages.success(request,'Login successfull')
            return redirect('home')
        else:
            print("user not here")
            messages.error(request,'Invalid username or password')
            
    all_messages = messages.get_messages(request)
    for message in all_messages:
        pass
    all_messages.used = True
        
    return render(request,'login.html')
        

@never_cache
@login_required(login_url='user_login')
def home(request):
    product = Product.objects.all()
    context = {
        'product':product
    }
    return render(request,'home.html',context)
        
        


def contact(request):
    if request.method=="POST":
        first_name = request.POST['first_name']
        phone_number = request.POST['number']
        message = request.POST['message']
        contact =Contact(
            first_name = first_name,
            phone_number = phone_number,
            message = message,
        )
        contact.save()
        return redirect('home')
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')



def ship(request):
    return render(request,'ship.html')


def single_product(request,id):
    products = Product.objects.filter(id=id)
    related = Product.objects.all()
    context = {
        'products':products,
        'related':related,
        
    }
    return render(request,'single_product.html',context)
    

def user_logout(request):
    logout(request)
    return redirect('index')