from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    '''student serializer'''
    
    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
        )
