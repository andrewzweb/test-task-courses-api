from django.db import models


class Course(models.Model):
    '''
    Course
    '''
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.name
