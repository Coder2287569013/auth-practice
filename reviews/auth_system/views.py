from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("review-list")
        else:
            messages.error(request, "Invalid information")
    else:
        form = UserCreationForm()
    
    return render(
        request, 
        "auth_system/register.html", 
        context={"form": form}
    )

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("review-list")
            else:
                messages.error(request, "Incorrect username or password")
    else:
        form = AuthenticationForm()
    
    return render(
        request,
        "auth_system/login.html",
        context={"form": form}
    )
