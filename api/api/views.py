from django.shortcuts import render
from django.http import JsonResponse
from . models import Student
from . serializers import StudentSerializers
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def index(request):
	if request.method=='GET':
		students=Student.objects.all()
		serializer=StudentSerializers(students,many=True)
		return JsonResponse(serializer.data,safe=False)
	elif request.method=='POST':
		serializer=StudentSerializers(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return JsonResponse()