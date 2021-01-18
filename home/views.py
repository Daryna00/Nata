from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def page(request):
    return render(request, 'home/page.html')

# Create your views here.
