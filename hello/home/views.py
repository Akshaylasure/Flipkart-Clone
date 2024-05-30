from django.shortcuts import render
from .models import Product, Electronic,Fashion,Child,Grocery  # Import both Product and Shou models
from datetime import datetime
from home.models import Contact
from django.contrib import messages


def index(request):
    products = Product.objects.all()  # Query all Product objects
    electronic = Electronic.objects.all()  # Query all Shou objects
    fashion  = Fashion.objects.all()
    child  = Child.objects.all()
    grocery = Grocery.objects.all()
    return render(request, 'index.html', {'products': products, 'electronic': electronic,'fashion':fashion,'child':child,'grocery':grocery})  # Pass both products and shous context




def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


