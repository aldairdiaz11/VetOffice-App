from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("owner/list", views.OwnerList.as_view(), name="ownerlist"),
    path("patient/list", views.PatientList.as_view(), name="patientlist"),
    path("owner/create", views.OwnerCreate.as_view(), name="ownercreate"),
    path("patient/create", views.PatientCreate.as_view(), name="patientcreate")
]
