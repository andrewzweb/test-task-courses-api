import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from mixer.backend.django import mixer
from ..models import Student
pytestmark = pytest.mark.django_db
from faker import Faker


@pytest.mark.django_db
class TestStudentReportInCSV:
    '''
    testcase report student in csv 
    '''

    def setup(self):
        self.client = APIClient()
        self.fake = Faker()

    def test_get_student_report_in_csv(self):
        
        student = mixer.blend('student.Student')
        
        response = self.client.get(
            reverse(
                'student:report_in_csv',
                kwargs={
                    'student_id': student.id,
                }
            ),
            format='json'
        )

        assert response.status_code == status.HTTP_200_OK

    def test_get_report_for_dont_exist_student(self):
        
        response = self.client.get(
            reverse(
                'student:report_in_csv',
                kwargs={
                    'student_id': self.fake.random_int(0, 100),
                }
            ),
            format='json'
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND
