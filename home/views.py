from django.shortcuts import render, HttpResponse
from datetime import  datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Cart
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Product,Order
from django.shortcuts import get_object_or_404

import re


# Create your views here.
def index(request):
    
    return render(request,'index.html')
def about(request):
    
   return render(request,'about.html')
def service(request):
    return render(request,'service.html')
   
def product(request):
    return render(request,'product.html')
def cart(request):
    return render(request,'cart.html')
    

@login_required
def profile(request):
    user = request.user

    orders = cart.objects.filter(user=user)

    return render(request, 'profile.html', {
        'user': user,
        'orders': orders
    })
    
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, "register.html")

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, "login.html")



def logout_view(request):
    logout(request)
    return redirect('home')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contact= Contact(name=name,email=email,phone=phone,message=message,
        date=datetime.today())
        contact.save()
        messages.success(request, "sent")
    return render(request,'contact.html')

def login_page(request):
    return render(request, 'login.html')


def register_page(request):
    return render(request, 'register.html')


def register_view(request):
    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        print("DATA:", username, email, password)  

        
        if not username:
            messages.error(request, "Username is required")
            return redirect("register")

        if not email:
            messages.error(request, "Email is required")
            return redirect("register")

        if not password:
            messages.error(request, "Password is required")
            return redirect("register")

        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")

        
        if len(password) < 8:
            messages.error(request, "Password must be 8+ characters")
            return redirect("register")

        if not re.search(r"[A-Za-z]", password):
            messages.error(request, "Password must contain letters")
            return redirect("register")

        if not re.search(r"[0-9]", password):
            messages.error(request, "Password must contain number")
            return redirect("register")

       
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect("login")

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.username}")
            return redirect("home")  
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, "login.html")

@login_required
def profile(request):
    return render(request, "profile.html", {"user": request.user})


@login_required
def update_profile(request):
    if request.method == "POST":
        user = request.user

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user.username = username
        user.email = email

        if password:
            if len(password) < 8:
                messages.error(request, "Password must be at least 8 characters long.")
                return redirect("profile")

            user.set_password(password)
            user.save()
            messages.success(request, "Password updated. Please login again.")
            return redirect("login")

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile")

    return redirect("profile")

def product(request):
    products = Product.objects.all()
    return render(request, "product.html", {"products": products})

    
@login_required
def cart(request):

    cart_items = Cart.objects.filter(user=request.user)

    cart_total = sum(item.get_total() for item in cart_items)

    shipping = 150

    total = cart_total + shipping

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "cart_total": cart_total,
        "shipping": shipping,
        "total": total
    })

@login_required
def add_to_cart(request):

    if request.method == "POST":

        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity"))
        size = request.POST.get("size")

        product = get_object_or_404(Product, id=product_id)

        Cart.objects.create(
            user=request.user,
            product=product,
            quantity=quantity,
            size=size
        )

        return redirect("cart")
    
@login_required
def update_cart(request, id):

    cart_item = get_object_or_404(Cart, id=id)

    if request.method == "POST":

        quantity = request.POST.get("quantity")

        cart_item.quantity = quantity
        cart_item.save()

    return redirect("cart")

def remove_from_cart(request, id):
    item = get_object_or_404(Cart, id=id)
    item.delete()
    return redirect("cart")

def checkout(request):
    return render(request, "checkout.html")


def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    cart_total = sum(item.get_total() for item in cart_items)

    shipping = 150

    final_total = cart_total + shipping

    if request.method == "POST":

        fullname = request.POST.get("fullname")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        notes = request.POST.get("notes")
        payment_method = request.POST.get("payment_method")

        
        for item in cart_items:

            Order.objects.create(
                user=request.user,
                product=item.product,
                size=item.size,
                quantity=item.quantity,

                fullname=fullname,
                address=address,
                phone=phone,

                payment_method=payment_method,
                 status='PENDING',
                total_price=item.get_total()
            )

        
        cart_items.delete()

        messages.success(request, "Order placed successfully!")

        return redirect("/")

    context = {
        "cart_items": cart_items,
        "cart_total": cart_total,
        "final_total": final_total,
    }

    return render(request, "checkout.html", context)


def previousorder(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    context = {
        'orders': orders
    }

    return render(request, 'previousorder.html', context)

def policy(request):
    return render(request, "policy.html")