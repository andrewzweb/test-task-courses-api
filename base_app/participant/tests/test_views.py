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
    testcase participant subscribe and unsubscribe to course 
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

    def test_unsubscribe_to_course(self):
        pass
