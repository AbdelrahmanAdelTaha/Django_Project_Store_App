from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from product.models import ProductTable
from product.forms import ProductForm
from django.views.generic.edit import UpdateView, CreateView
# Create your views here.

def contact_us (request):
    return render(request, "product/contactus.html")
def about_us (request):
    return render(request, "product/aboutus.html")
def productIndex(request):
    all_products = [
        {"id": 1, "name": "mobile", "description": "Description for mobile", "image": "mobile.png", "no_of_item": '5'},
        {"id": 2, "name": "laptop", "description": "Description for laptop", "image": "laptop.png", "no_of_item": '9'},
        {"id": 3, "name": "playstation", "description": "Description for playstation", "image": "playstation.png", "no_of_item": '6'}
    ]
    return render(request, "product/allproducts.html", context={"products": all_products})

def index(request):
    products = ProductTable.objects.all()
    return render(request, 'product/index.html', {"products": products})

def show(request, id):
    product = ProductTable.objects.get(pk=id)
    return render(request, "product/show.html", {"product": product})

def delete(request, id):
    product = ProductTable.objects.get(pk=id)
    product.delete()
    return redirect("/product")

class CreateProductView(CreateView):
    model = ProductTable
    form_class = ProductForm
    template_name = 'product/create.html'
    success_url = '/product'

class UpdateProductView(UpdateView):
    model = ProductTable
    form_class = ProductForm
    template_name = 'product/edit.html'
    success_url = '/product'

