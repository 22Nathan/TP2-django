from django.urls import path
from .views import *

urlpatterns = [
    path('animals/', getAnimals),
    path('addAnimals/', addAnimal),
    path('updateAnimals/<int:id>', updateAnimal),
    path('deleteAnimals/<int:id>', deleteAnimal),
]
