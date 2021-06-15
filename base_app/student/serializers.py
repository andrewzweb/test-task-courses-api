from rest_framework import serializers
from .models import Student
from participant.models import CourseParticipant

class StudentSerializer(serializers.ModelSerializer):
    '''student serializer'''
    
    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
        )

class StudentReportSerializer(serializers.ModelSerializer):
    '''student report serializer'''

    count_courses = serializers.SerializerMethodField()
    count_completed_courses = serializers.SerializerMethodField()
    
    class Meta:
        model = Student
        fields = (
            'id',
            'full_name',
            'count_courses',
            'count_completed_courses',
        )

    def get_count_courses(self, instance):
        print('instance', instance.id)
        count = CourseParticipant.objects.filter(student__id=instance.id).count()
        return count
        
    def get_count_completed_courses(self, instance):
        count = CourseParticipant.objects.filter(student__id=instance.id, completed=True).count()
        return count
