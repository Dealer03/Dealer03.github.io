from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.forms import RegistrationForm
from .models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.

@login_required(login_url="/login/")
def home(request):
    getUser = User.objects.all()
    userDict = {'name': getUser}
    return render(request, 'main/home.html', userDict)


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {"form": form})
