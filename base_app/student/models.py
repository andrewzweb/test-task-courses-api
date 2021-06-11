from django.db import models


class Student(models.Model):
    '''
    Entity student
    '''

    first_name = models.CharField(verbose_name='student first name', max_length=64)
    last_name = models.CharField(verbose_name='student last name', max_length=64)
    email = models.EmailField()

    class Meta:
        db_table = 'student'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
