from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import AnimalSerializer, AnimalTypeSerializer
from rest_framework import status

# Create your views here.

# --------------------------------------------------------------------------------
@api_view(['GET'])
def getAnimals(request):
    lesAnimaux = Animal.objects.all()[:10] 
    serializer = AnimalSerializer(lesAnimaux, many=True)
    return Response(serializer.data)

# --------------------------------------------------------------------------------
@api_view(['GET'])
def getCategoriesAnimals(request):
    lesTypesAnimaux = AnimalType.objects.all() 
    serializer = AnimalTypeSerializer(lesTypesAnimaux, many=True)
    return Response(serializer.data)

# --------------------------------------------------------------------------------

@api_view(['GET'])
def getAnimalsById(request, id):
    animal = Animal.objects.get(id=id) 
    serializer = AnimalSerializer(animal)
    return Response(serializer.data)

# --------------------------------------------------------------------------------

@api_view(['POST'])
def addAnimal(request):
    serializer = AnimalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# --------------------------------------------------------------------------------

@api_view(['PUT'])
def updateAnimal(request, id):
    try:
        animal = Animal.objects.get(id=id)
    except Animal.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = AnimalSerializer(animal,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --------------------------------------------------------------------------------

@api_view(['DELETE'])
def deleteAnimal(request, id):
    try:
        animal = Animal.objects.get(id=id)
    except Animal.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    serializer = AnimalSerializer(animal)
    animal.delete()
    return Response(serializer.data)

# --------------------------------------------------------------------------------

@api_view(['GET'])
def getNbAnimals(request):
    animaux = Animal.objects.all()
    return Response(len(animaux))