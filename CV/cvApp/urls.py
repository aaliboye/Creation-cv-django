from os import name
from django.urls import path
from cvApp.views import download, formulaire, generer, index, verification


urlpatterns = [
    path('', index, name="acceuil"),
    path('creercv', formulaire, name="creer"),
    path('verification', verification, name="verification"),
    path('<int:id>', generer, name="generer"),
    path('download', download, name="download"),
]