import pytest
import datetime
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from course.models import Course


class TestCourses:
    ''' testcase courses '''

    def test_create_course(self):
        '''test create course by default'''
        obj = mixer.blend('course.Course')
        assert obj.id == 1
        assert obj.name
        assert obj.description

    def test_course_have_custom_name(self):
        '''test course have cusom name'''
        obj = mixer.blend('course.Course')
        assert str(obj) in str(Course.objects.first())
        
    def test_course_set_any_start_date(self):
        '''test set any start date'''

        course_name = str(mixer.RANDOM)
        start_date = datetime.date.today()
        end_date = datetime.date.today() + datetime.timedelta(days=1)
        obj = mixer.blend(Course,
            name=course_name,
            start_date=start_date,
            end_date=end_date
        )
        assert course_name in  obj.name
        assert obj.start_date == start_date
        assert obj.end_date == end_date
