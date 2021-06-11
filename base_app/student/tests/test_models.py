import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from ..models import Student


class TestStudent:
    '''
    Testcase for model student
    '''
    
    def test_create_student(self):
        '''test create student'''
        obj = mixer.blend('student.Student')
        assert obj.id == 1
        assert obj.first_name
        assert obj.last_name
        assert obj.email
        
        assert obj in Student.objects.all()

    def test_first_name_and_last_name_is_obj_name(self):
        obj = mixer.blend('student.Student')
        
        assert obj.first_name in str(obj)
        assert obj.last_name in str(obj)
