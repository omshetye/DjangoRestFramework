# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from . serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# def studentsView(request):
#   students = Student.objects.all()
#   student_list = []
#   for student in students.values():
#     student_list.append(student)
#   print(student_list)
#   return JsonResponse(student_list, safe=False)

# DRF Serialization

@api_view(['GET'])
def studentsView(request):
  if request.method == 'GET':
    # Get all data from Student table
    students = Student.objects.all()
    serializer = StudentSerializer(instance=students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'POST':
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)