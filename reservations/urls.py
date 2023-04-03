from django.urls import path
from . import views

urlpatterns = [
    path("connexion/", views.connexion, name="connexion"),
    path("home/", views.home, name="home"),
    path("reservation/", views.reservation, name="reservation"),
    path("ecole/<int:ecole_id>/", views.ecole, name="ecole"),
]
