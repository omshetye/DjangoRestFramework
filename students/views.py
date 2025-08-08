from django.shortcuts import render
from django.http import HttpResponse

def students(request):
  students = [
    {"id": "01", "name": "Om", "age": 22}
    ]
  return HttpResponse(students)
