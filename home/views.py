from django.shortcuts import render, HttpResponse
from datetime import  datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request,'index.html')
def about(request):
    
   return render(request,'about.html')
def service(request):
    return render(request,'service.html')
   
def product(request):
    return render(request,'product.html')
    



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