from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from cursos.models import Course, Rating
from cursos.serializer import CourseSerializer, RatingSerializer


class CourseAPIView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)


class RatingAPIView(APIView):
    def get(self, resquest):
        rating = Rating.objects.all()
        serializer = RatingSerializer(rating, many=True)
        return Response(serializer.data)
