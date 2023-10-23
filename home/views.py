from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse('<h1>Welcome To our page</h1>')
