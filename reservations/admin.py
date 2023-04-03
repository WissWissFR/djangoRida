from django.contrib import admin
from .models import Ecole, Reservation

# Register your models here.
@admin.register(Ecole)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(Reservation)
class AuthorAdmin(admin.ModelAdmin):
    pass