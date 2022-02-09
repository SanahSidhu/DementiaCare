from django.urls import path
from .views import (
    EmergencyContacts,
    RemindersAlerts,
    Inventory,
    CheckList,
    Calendar,
    MedList,
    SignUp,
    Login,
    Media,
    Notes,
)

urlpatterns = [
    path("signup", SignUp.as_view()),
    path("login", Login.as_view()),
    path("checklist", CheckList.as_view()),
    path("notes", Notes.as_view()),
    path("media", Media.as_view()),
    path("medlist", MedList.as_view()),
    path("inventory", Inventory.as_view()),
    path("calendar", Calendar.as_view()),
    path("reminderalerts", RemindersAlerts.as_view()),
    path("emergencycontacts", EmergencyContacts.as_view()),
]
