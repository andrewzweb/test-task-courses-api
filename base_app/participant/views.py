from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from course.models import Course
from .serializers import ParticipantSerializer
from .models import CourseParticipant
from student.models import Student

@api_view(['POST', 'DELETE'])
def participant_detail(request, course_id, student_id):

    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
        else:
            Response(
            {'data': serializer.data},
            status = status.HTTP_400_BAD_REQUEST
        )

        return Response(
            {'data': serializer.data},
            status = status.HTTP_201_CREATED
        )

    elif request.method == 'DELETE':
        try: 
            participant = CourseParticipant.objects.get(
                course__id=course.id,
                student__id=student.id
            )
            participant.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except: 
            return Response(status = status.HTTP_400_BAD_REQUEST)
