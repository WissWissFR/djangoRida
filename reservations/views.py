from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Ecole, Reservation
from datetime import datetime

def connexion(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "reservations/connexion.html")

@login_required
def home(request):
    ecoles = Ecole.objects.all()
    return render(request, "reservations/home.html", {"ecoles": ecoles})

@login_required
def reservation(request):
    if request.method == "POST":
        ecole_id = request.POST["ecole_id"]
        date_str = request.POST["date"]
        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M')
        ecole = Ecole.objects.get(id=ecole_id)

        reservation = Reservation(ecole=ecole, client=request.user, date=date_obj)
        reservation.save()
        
        return redirect("ecole", ecole_id=ecole_id)
    ecoles = Ecole.objects.all()
    return render(request, "reservations/reservation.html", {"ecoles": ecoles})

@login_required
def ecole(request, ecole_id):
    ecole = Ecole.objects.get(id=ecole_id)
    reservations = Reservation.objects.filter(ecole=ecole)
    return render(request, "reservations/ecole.html", {"ecole": ecole, "reservations": reservations})
