from django.contrib import admin
from .models import CourseParticipant


@admin.register(CourseParticipant)
class CourseParticipantAdmin(admin.ModelAdmin):
    '''course participant admin'''
    
    list_display = (
        'id',
        'course',
        'student',
        'completed'
    )

    search_fields = ('course', 'student')
    list_filter = ('course', 'completed')
