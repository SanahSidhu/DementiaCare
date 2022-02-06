from django.urls import path
from .views import CheckList, Inventory, Login, MedList, Media

urlpatterns = [
    path("login", Login.as_view()),
    path("checklist", CheckList.as_view()),
    path("media", Media.as_view()),
    path("medlist", MedList.as_view()),
    path("inventory", Inventory.as_view()),
]