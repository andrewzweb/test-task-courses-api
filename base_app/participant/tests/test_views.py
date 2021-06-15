import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.parsers import JSONParser
from mixer.backend.django import mixer
from ..models import CourseParticipant
from ..views import participant_detail
pytestmark = pytest.mark.django_db
from faker import Faker


@pytest.mark.django_db
class TestParticipantSubscribeToCourse:
    '''
    testcase participant subscribe to course 
    '''

    def setup(self):
        self.client = APIClient()
        self.fake = Faker()

    def test_subscribe_to_course(self):
        course = mixer.blend('course.Course')
        student = mixer.blend('student.Student')
        
        response = self.client.post(
            reverse(
                'participant:participant_subscribe',
                kwargs={
                    'course_id': course.id,
                    'student_id': student.id,
                }
            ),
            data = {
                'course': course.id,
                'student': student.id
            }, 
            format='json'
        )
        
        assert response.status_code == 201
        assert CourseParticipant.objects.count() == 1

    def test_dont_create_participant_when_instance_student_dont_exist(self):      
        course = mixer.blend('course.Course')
        
        response = self.client.post(
            reverse(
                'participant:participant_subscribe',
                kwargs={
                    'course_id': course.id,
                    'student_id': self.fake.random_int(0, 100),
                }
            ),
            data = {
                'course': course.id,
            }, 
            format='json'
        )
        
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert CourseParticipant.objects.count() == 0

    def test_dont_create_participant_when_instance_course_dont_exist(self):
        student = mixer.blend('student.Student')
        
        response = self.client.post(
            reverse(
                'participant:participant_subscribe',
                kwargs={
                    'course_id': self.fake.random_int(0, 100),
                    'student_id': student.id,
                }
            ),
            data = {
                'student': student.id,
            }, 
            format='json'
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert CourseParticipant.objects.count() == 0

    def test_send_not_valid_data(self):
        
        course = mixer.blend('course.Course')
        student = mixer.blend('student.Student')
        
        response = self.client.post(
            reverse(
                'participant:participant_subscribe',
                kwargs={
                    'course_id': course.id,
                    'student_id': student.id,
                }
            ),
            data = {
                'course': self.fake.name(),
                'student': self.fake.random_int(10,100),
            }, 
            format='json'
        )
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert CourseParticipant.objects.count() == 0
        

@pytest.mark.django_db
class TestParticipantUnsubscribe:
    '''
    testcase participant unsubscribe from course 
    '''

    def setup(self):
        self.client = APIClient()
        self.fake = Faker()

    def test_unsubscribe_student_form_course(self):

        student = mixer.blend('student.Student')
        course = mixer.blend('course.Course')
        mixer.blend(
            'participant.CourseParticipant',
            course=course,
            student=student
        )

        assert CourseParticipant.objects.count() == 1

        response = self.client.delete(
            reverse(
                'participant:participant_unsubscribe',
                kwargs={
                    'course_id': course.id,
                    'student_id': student.id,
                }
            ),
            data = {
                'student': student.id,
                'course': course.id,
            }, 
            format='json'
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert CourseParticipant.objects.count() == 0

    def test_try_delete_dont_exist_participant(self):

        student = mixer.blend('student.Student')
        course = mixer.blend('course.Course')
        
        response = self.client.delete(
            reverse(
                'participant:participant_unsubscribe',
                kwargs={
                    'course_id': course.id,
                    'student_id': student.id,
                }
            ),
            format='json'
        )
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
