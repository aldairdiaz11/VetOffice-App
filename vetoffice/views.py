# from django.shortcuts import render
from .models import Owner, Patient
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import OwnerCreateForm, PatientCreateForm, OwnerUpdateForm, PatientUpdateForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

pets = [
    {'petname': 'Fido', 'animal_type': 'dog'},
    {'petname': 'Clementine', 'animal_type': 'cat'},
    {'petname': 'Cleo', 'animal_type': 'cat'},
    {'petname': 'Oreo', 'animal_type': 'dog'},
]


# Create your views here.
class Home(TemplateView):
    template_name = "vetoffice/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # context["name"] = request.user
        return context


class OwnerList(LoginRequiredMixin, ListView):
    model = Owner
    template_name = "vetoffice/owner_list.html"


class PatientList(ListView, LoginRequiredMixin):
    model = Patient
    template_name = "vetoffice/patient_list.html"


class OwnerCreate(CreateView):
    model = Owner
    template_name = "vetoffice/owner_create_form.html"
    form_class = OwnerCreateForm


class PatientCreate(CreateView):
    model = Patient
    template_name = "vetoffice/patient_create_form.html"
    form_class = PatientCreateForm


class OwnerUpdate(UpdateView, LoginRequiredMixin):
    model = Owner
    template_name = "vetoffice/owner_update_form.html"
    form_class = OwnerUpdateForm


class PatientUpdate(UpdateView, LoginRequiredMixin):
    model = Patient
    template_name = "vetoffice/patient_update_form.html"
    form_class = PatientUpdateForm


class OwnerDelete(DeleteView, LoginRequiredMixin):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"


class PatientDelete(DeleteView, LoginRequiredMixin):
    model = Patient
    template_name = "vetoffice/patient_delete_form.html"


# Login and authenticate
def login_view(request):
    context = {
        "login_view": "active"
    }
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request=request, user=user)
            return redirect("home")
        else:
            return HttpResponse("invalid credentials")

    return render(request, "registration/login.html", context)


def logout_view(request):
    logout(request)
    return redirect('home')


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
