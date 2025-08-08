from django.shortcuts import render
from django.http import JsonResponse

def studentsView(request):
  students = {
    'id': 1,
    'name': 'Om',
    'age': 22
  }
  return JsonResponse(students)
