from django.shortcuts import render
from main.models import Product , Programm
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request , 'home.html')

def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request , 'all_products.html' , context)

def all_programs(request):
    if request.method == 'GET':
        programs = Programm.objects.exclude(category = 'Detox программа')
        context = {
            'programs': programs
        }
        return render(request , 'all_programs.html' , context)

def slim_programs(request):
    if request.method == 'GET':
        programs = Programm.objects.filter(category = 'Для похудения')
        context = {
                'programs': programs
            }
        return render(request , 'slim_programs.html' , context)

def detox_programs(request):
    if request.method == 'GET':
        programs = Programm.objects.filter(category = 'Detox программа')
        context = {
                'programs': programs
            }
        return render(request , 'detox_programs.html' , context)