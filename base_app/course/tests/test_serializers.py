import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from ..serializers import CourseSerializer

from ..models import Course
from student.models import Student
from participant.models import CourseParticipant


@pytest.mark.django_db
class TestCourseSerializer:
    '''testcase course serializer'''
    
    def test_course_serializer_show_10_students(self):
        '''test serializer'''
        students = mixer.cycle(15).blend('student.Student')
        course = mixer.blend('course.Course')
        for student in students:
            mixer.blend(
                'participant.CourseParticipant',
                course=course,
                student=student
            )

        assert CourseParticipant.objects.count() == 15
        assert Course.objects.count() == 1
        assert Student.objects.count() == 15
        
        serialiser = CourseSerializer(Course.objects.all(), many=True)
        assert len(serialiser.data[-1]['courses']) == 10
