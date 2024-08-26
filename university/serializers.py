from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data.get['first_name', ''],
            last_name=validated_data.get['last_name', ''],
            email=validated_data.get['email', ''],
            password=validated_data['password']
        )
        return user


class StudentSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField()

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        student_id_str = validated_data.pop('student_id')
        student_id_obj, created = StudentID.objects.get_or_create(student_id=student_id_str)
        validated_data['student_id'] = student_id_obj
        
        return Student.objects.create(**validated_data)
    
    
        
class UniSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = uni
        fields = '__all__'    
        
class DepSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Department
        fields = '__all__'  
        
class Subject_Marks_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject_Marks
        fields = '__all__'   
        
class ReportCard_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReportCard
        fields = '__all__'   