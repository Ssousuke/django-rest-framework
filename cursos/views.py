from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cursos.models import Course, Rating
from cursos.serializer import CourseSerializer, RatingSerializer


class CourseAPIView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RatingAPIView(APIView):
    def get(self, resquest):
        rating = Rating.objects.all()
        serializer = RatingSerializer(rating, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
