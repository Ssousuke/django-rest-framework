from rest_framework import serializers
from cursos.models import Course, Rating


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'course_author',
            'url',
            'free',
        )


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Rating
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'grade',
            'created',
            'activated',
        )
