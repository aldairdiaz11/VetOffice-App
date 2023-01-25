from django.shortcuts import render
from .models import Owner, Patient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class OwnerCreate(CreateView):
    model = Owner
    template_name = "vetoffice/owner_create_form.html"
    fields = ["first_name", "last_name", "phone"]


class PatientCreate(CreateView):
    model = Patient
    template_name = "vetoffice/patient_create_form.html"
    fields = ["animal_type", "breed", "pet_name", "age", "owner"]


class OwnerUpdate(UpdateView):
    model = Owner
    template_name = "vetoffice/owner_update_form.html"
    fields = ["first_name", "last_name", "phone"]


class PatientUpdate(UpdateView):
    model = Patient
    template_name = "vetoffice/patient_update_form.html"
    fields = ["animal_type", "breed", "pet_name", "age", "owner"]


class OwnerDelete(DeleteView):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"


class PatientDelete(DeleteView):
    model = Patient
    template_name = "vetoffice/patient_delete_form.html"
