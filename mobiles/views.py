from django.shortcuts import render
from .models import Mobiles
# Create your views here.
def index(request):
    return render(request,'store/index.html')
def about (request):
    return render(request,'store/about.html')
def sign(request):
    return render(request,'store/sign.html')
def products(request):
    return render(request,'store/products.html',{'mob':Mobiles.objects.all()})