from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import MenTop, MenSneakers, LadiesClothing
from .forms import RegistrationForm

# Create your views here.

def homepage(request):
    mentop = MenTop.objects.all()
    
    latest_items_table1 = MenTop.objects.order_by('-time')[:5]
    latest_items_table2 = MenSneakers.objects.order_by('-time')[:5]
    latest_items_table3 = LadiesClothing.objects.order_by('-time')[:5]
    latest_items = list(latest_items_table1) + list(latest_items_table2) + list(latest_items_table3)

    context = {
        'latest_items': latest_items,
        'mentop': mentop
    }
    return render(request, 'home.html', context)





def registerPage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # The form is valid, proceed with user registration
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, password=password, email=email)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # Optionally, log the user in
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return redirect('login')  # Adjust the URL name as needed
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', {'form': form})



def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirect to the home page after successful login
        else:
            # Handle authentication failure, e.g., display an error message
            pass

    return render(request, 'signin.html')




# def loginPage(request):
#     pass


# def logoutPage(request):
#     pass
