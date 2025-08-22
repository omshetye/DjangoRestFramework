# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from employees.models import Employee
from . serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import Http404
from rest_framework import mixins, generics

# def studentsView(request):
#   students = Student.objects.all()
#   student_list = []
#   for student in students.values():
#     student_list.append(student)
#   print(student_list)
#   return JsonResponse(student_list, safe=False)

# DRF Serialization

@api_view(['GET', 'POST'])
def studentsView(request):
  if request.method == 'GET':
    # Get all data from Student table
    students = Student.objects.all()
    serializer = StudentSerializer(instance=students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  elif request.method == 'POST':
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
  try:
    student = Student.objects.get(pk=pk)
  except Student.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = StudentSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)
 
  elif request.method == 'PUT':
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  elif request.method == 'DELETE':
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
# class employeeView(APIView):
#   def get(self, request):
#     employees = Employee.objects.all()
#     serializer = EmployeeSerializer(instance=employees, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)
  
#   def post(self, request):
#     serializer = EmployeeSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class employeeDetailView(APIView):
#   def getObject(self, pk):
#     try:
#       employee = Employee.objects.get(pk=pk)
#       return employee
#     except Employee.DoesNotExist:
#       raise Http404
    
#   def get(self, request, pk):
#       employee = self.getObject(pk)
#       serializer = EmployeeSerializer(employee)
#       return Response(serializer.data, status=status.HTTP_200_OK)
  
#   def put(self, request, pk):
#     employee = self.getObject(pk)
#     serializer = EmployeeSerializer(employee, request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#   def delete(self, request, pk):
#     employee = self.getObject(pk)
#     employee.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT) 

class employeeView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
  queryset =  Employee.objects.all()
  serializer_class = EmployeeSerializer

  def get(self, request):
    return self.list(request)
  
  def post(self, request):
    return self.create(request)
  
class employeeDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
  queryset = Employee.objects.all()
  serializer_class = EmployeeSerializer

  def get(self, request, pk):
    return self.retrieve(request, pk)
  
  def put(self, request, pk):
    return self.update(request, pk)
  
  def delete(self, request, pk):
    return self.destroy(request, pk)
