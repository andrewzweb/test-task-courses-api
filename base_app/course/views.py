from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Course
from .serializers import CourseSerializer


@api_view(['GET'])
def courses_list(request):
    if request.method == 'GET':
        serializer = CourseSerializer(Course.objects.all(), many=True)
        return Response({'data': serializer.data})
