from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    '''student admin'''
    
    list_display = (
        'first_name',
        'last_name',
        'email',
    )

    search_fields = ('first_name', 'last_name', 'email')
