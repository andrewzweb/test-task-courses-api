from rest_framework import serializers
from .models import Course
from participant.serializers import CourseParticipantSerializer
from participant.models import CourseParticipant
from student.models import Student


class CourseSerializer(serializers.ModelSerializer):
    '''courses serializer'''

    courses = CourseParticipantSerializer(
        CourseParticipant.objects.all(),
        many=True
    )
    all_count_students = serializers.SerializerMethodField()

        
    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'description',
            'start_date',
            'end_date',
            'all_count_students',
            'courses',
        )

    def get_all_count_students(self, instance):
        count = 0
        try:
            count = len(self.instance.data['courses'])
        except:
            count = 0
        return count

    def to_representation(self, instance):
        data = super(CourseSerializer, self).to_representation(instance)
        only_ten_items = data['courses'][:10]
        data['courses'] = only_ten_items
        return data
