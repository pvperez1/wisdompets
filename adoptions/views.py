from django.shortcuts import render
from django.http import HttpResponse
from .models import Pet
# Create your views here.

def home(request):
    Pets = Pet.objects.all()
    return render(request, "home.html", {'pets':Pets})

def pet_detail(request, pet_id):
    pet = Pet.objects.get(pk=pet_id)
    return render(request, "pet_detail.html", {'pet':pet})
