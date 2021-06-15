from rest_framework import serializers
from .models import CourseParticipant
from student.serializers import StudentSerializer 
from student.models import Student


class CourseParticipantSerializer(serializers.ModelSerializer):
    '''courses participant serializer'''

    student = StudentSerializer(many=False)

    class Meta:
        model = CourseParticipant
        fields = ('id', 'student')
