from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return redirect ('http://127.0.0.1:8000/admin')
    #return render(request, "registrations/login.html")
    