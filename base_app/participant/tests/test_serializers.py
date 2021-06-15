import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from ..models import CourseParticipant
from ..serializers import CourseParticipantSerializer


@pytest.mark.django_db
class TestCourseParticipantSerializer:

    def test_serializer(self):
        students = mixer.cycle(15).blend('student.Student')
        course = mixer.blend('course.Course')
        for student in students:
            mixer.blend(
                'participant.CourseParticipant',
                course=course,
                student=student
            )

        query = CourseParticipant.objects.all()
        
        serializer = CourseParticipantSerializer(query, many=True)
        print(serializer)
        print(len(serializer.data))
        
        assert len(serializer.data) == len(query)

