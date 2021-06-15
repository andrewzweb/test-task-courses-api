from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/courses/', include('course.urls', namespace='courses')),
    path('api/participant/', include('participant.urls', namespace='participant')),
]
