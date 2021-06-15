from django.db import models
from student.models import Student
from course.models import Course


class CourseParticipant(models.Model):
    '''
    CourseParticipant
    '''
    course = models.ForeignKey(
        Course,
        related_name='courses',
        on_delete=models.CASCADE
    )
    student = models.ForeignKey(
        Student,
        related_name='student_name',
        on_delete=models.CASCADE
    )
    completed = models.BooleanField(null=False, default=False)

    class Meta:
        unique_together = [['student', 'course']]
        db_table = 'course_participant'

    def __str__(self):
        return '{} {}'.format(self.course, self.student)
