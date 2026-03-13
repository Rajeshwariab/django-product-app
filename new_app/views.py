from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser




# Create your views here.
def home(requests):
    return render(requests,'home.html') 




# READ (Display all products)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})




# CREATE
def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')


        Product.objects.create(
            name=name,
            price=price,
            description=description
        )
        return redirect('product_list')


    return render(request, 'add_product.html')




# UPDATE
def edit_product(request, id):
    product = Product.objects.get(id=id)


    if request.method == "POST":
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.save()
        return redirect('product_list')


    return render(request, 'edit_product.html', {'product': product})




# DELETE
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product_list')



# REGISTER VIEW
def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
   
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        gmail = request.POST.get('gmail')
        phonenumber = request.POST.get('phonenumber')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
       
        if password != password_confirm:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
       
        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})       
        user = CustomUser.objects.create_user(
            username=username,
            name=name,
            email=gmail,
            password=password,
            phone_number=phonenumber
        )
        login(request, user)
        return redirect('home')
   
    return render(request, 'register.html')


# LOGIN VIEW
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
   
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})   
    return render(request, 'login.html')


# LOGOUT VIEW
def logout_user(request):
    logout(request)
    return redirect('login')