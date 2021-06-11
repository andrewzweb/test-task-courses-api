import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from ..models import CourseParticipant
from student.models import Student
from course.models import Course


class TestCourseParticipant:
    '''
    Testcase CourseParticipant
    '''
    
    def test_create_course_participant(self):
        '''test create course participant'''
        student = mixer.blend('student.Student')
        course = mixer.blend('course.Course')
        participant = mixer.blend(
            'participant.CourseParticipant',
            course = course,
            student = student
        )

        assert CourseParticipant.objects.first() == participant
        assert CourseParticipant.objects.first().id == participant.id
        assert CourseParticipant.objects.first().completed == False

    def test_course_participant_have_custom_name(self):
        '''course participant have custom name'''
        student = mixer.blend('student.Student')
        course = mixer.blend('course.Course')
        participant = mixer.blend(
            'participant.CourseParticipant',
            course = course,
            student = student
        )

        assert str(student) in str(CourseParticipant.objects.first())
        assert str(course) in str(CourseParticipant.objects.first())
        
    def test_one_course_can_have_many_students(self):
        '''test one course can have many students'''
        students = mixer.cycle(5).blend('student.Student')
        assert Student.objects.count() == 5
        
        course = mixer.blend('course.Course')
        assert Course.objects.count() == 1

        for student in students: 
            mixer.blend(
                'participant.CourseParticipant',
                course = course,
                student = student
        )
        assert CourseParticipant.objects.count() == 5
        assert len(CourseParticipant.objects.filter(course=course)) == 5

    def test_one_student_can_have_many_courses(self):
        '''test one student can have many courses'''
        
        student = mixer.blend('student.Student')
        assert Student.objects.count() == 1
        
        courses = mixer.cycle(5).blend('course.Course')
        assert Course.objects.count() == 5

        for course in courses: 
            mixer.blend(
                'participant.CourseParticipant',
                course = course,
                student = student
        )
        assert CourseParticipant.objects.count() == 5
        assert len(CourseParticipant.objects.filter(student=student)) == 5
