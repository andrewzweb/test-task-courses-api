from django.urls import path
from .views import *


app_name='student'

urlpatterns = [
    path('<int:student_id>/report/', student_report, name='report_in_csv'),
]
