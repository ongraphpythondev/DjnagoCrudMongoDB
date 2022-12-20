from django.shortcuts import render
from rest_framework import viewsets
from .serializers import studentSerializer,teacherSerializer
from .models import Teacher,Students
# Create your views here.

class CRUDStudentView(viewsets.ModelViewSet):
    serializer_class= studentSerializer
    queryset = Students.objects.all()

class CRUDTeacherView(viewsets.ModelViewSet):
    serializer_class= teacherSerializer
    queryset = Teacher.objects.all()