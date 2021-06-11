from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    '''course admin'''
    
    list_display = (
        'name',
        'description',
        'start_date',
        'end_date'
    )

    search_fields = ('name', 'description')
    list_filter = ('start_date', 'end_date')
