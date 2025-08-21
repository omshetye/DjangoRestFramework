from django.urls import path
from . import views

urlpatterns = [
  path('students/', views.studentsView),
  path('students/<int:pk>/', views.studentDetailView),
  path('employees/', views.employeeView.as_view()),
  path('employees/<int:pk>/', views.employeeDetailView.as_view()),
]