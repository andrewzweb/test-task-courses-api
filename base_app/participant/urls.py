from django.urls import path
from .views import *


app_name='participant'

urlpatterns = [
    path('<int:course_id>/<int:student_id>/subscribe', participant_detail, name='participant_subscribe'),
    path('<int:course_id>/<int:student_id>/unsubscribe', participant_detail, name='participant_unsubscribe'),
]
