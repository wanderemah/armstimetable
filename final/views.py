from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def home(request):
    return render(request, 'home.html')


@login_required
def logout(request):
    logout
    return redirect('home')


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        # password.set_password(password)
        # after grabbing the fields we need to autheticate
        user = authenticate(username=user_name, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('timetable:docket'))
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return render(request, 'login.html', {'form': login})
