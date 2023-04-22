from django.shortcuts import render
from django.http import HttpResponse
from .models import Goods

# Create your views here.

def index(request):
    products = Goods.objects.all()
    return render(request, 'index.html', {'products': products})



def about(request):
    return render(request, 'about.html')
#
# def new_page(request):
#     return render(request, 'main/new_page.html')