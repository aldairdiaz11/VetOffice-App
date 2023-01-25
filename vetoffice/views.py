from django.shortcuts import render
from .models import Owner, Patient
from django.views.generic import ListView
# from django.http import HttpResponse


pets = [
    {'petname': 'Fido', 'animal_type': 'dog'},
    {'petname': 'Clementine', 'animal_type': 'cat'},
    {'petname': 'Cleo', 'animal_type': 'cat'},
    {'petname': 'Oreo', 'animal_type': 'dog'},
]


# Create your views here.
def home(request):
    context = {
        "name": "Aldair",
        "pets": pets
        }
    return render(request, "vetoffice/home.html", context=context)


class OwnerList(ListView):
    model = Owner
    template_name = "vetoffice/owner_list.html"


class PatientList(ListView):
    model = Patient
    template_name = "vetoffice/patient_list.html"
