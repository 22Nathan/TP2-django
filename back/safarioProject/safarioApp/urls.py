from django.urls import path
from .views import *

urlpatterns = [
    path('animals/', getAnimals),
    path('categories/', getCategoriesAnimals),
    path('addAnimals', addAnimal),
    path('updateAnimals/<int:id>', updateAnimal),
    path('deleteAnimals/<int:id>', deleteAnimal),
    path('animal/<int:id>', getAnimalsById),
    path('nbAnimals/', getNbAnimals),
]
