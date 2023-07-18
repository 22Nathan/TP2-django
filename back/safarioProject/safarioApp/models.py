from django.db import models

# Create your models here.
class Animal(models.Model):
    nom = models.CharField(max_length=50)
    ageMax = models.IntegerField()
    avgWeight = models.CharField(max_length=20)
    nomS = models.CharField(max_length=120)
    typeAnimal = models.CharField(max_length=100)
    categorieAnimal = models.ForeignKey('AnimalType', on_delete=models.DO_NOTHING)


class AnimalType(models.Model):
    type = models.CharField(max_length=50, choices=[("Mammifères", "Mammifères"), ("Oiseaux", "Oiseaux"), ("Poissons", "Poissons")])
