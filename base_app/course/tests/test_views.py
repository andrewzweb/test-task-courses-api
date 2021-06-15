import pytest
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from rest_framework.parsers import JSONParser
from django.urls import reverse
pytestmark = pytest.mark.django_db
from ..models import Course
from ..views import courses_list
import io
import random


@pytest.mark.django_db
class TestCourseViews:

    def setup(self):
        self.client = APIClient()

    
    def test_get_list_courses(self):

        count_courses = random.randint(1,20)
        mixer.cycle(count_courses).blend(
            'course.Course'
        )
        
        response = self.client.get(
            reverse('course:courses_list'),
            format='json'
        )

        assert response.status_code == 200
        stream = io.BytesIO(response.content)
        data = JSONParser().parse(stream)
        assert len(data['data']) == count_courses
