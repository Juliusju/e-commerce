from django.shortcuts import render, HttpResponse
from .models import MenTop

# Create your views here.

def homepage(request):
    mentop = MenTop.objects.all()
    context = {
        'mentop': mentop
    }
    return render(request, 'home.html', context)

# def registerPage(request):
#     pass


# def loginPage(request):
#     pass


# def logoutPage(request):
#     pass
