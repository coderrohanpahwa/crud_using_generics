from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import Student,StudentSerializer
# Create your views here.
class StudentListCreate(ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
class StudentRUD(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
