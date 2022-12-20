from rest_framework import serializers
from .models import Students,Teacher

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id','name','rollno','standard','teacher']

class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','name','department','salary']