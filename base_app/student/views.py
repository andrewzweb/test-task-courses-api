from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from student.models import Student
from .serializers import StudentReportSerializer
from rest_framework_csv.renderers import CSVRenderer

class StudentReportRenderer(CSVRenderer):
    '''Add header fot csv file'''
    header = ['id', 'full_name', 'count_courses', 'count_completed_courses' ]


@api_view(['GET'])
@renderer_classes((StudentReportRenderer,))
def student_report(request, student_id):

    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StudentReportSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)
