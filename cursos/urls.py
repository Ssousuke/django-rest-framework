from django.urls import path
from cursos import views


urlpatterns = [
    path('courses/', views.CourseAPIView.as_view(), name='courses'),
    path('rating/', views.RatingAPIView.as_view(), name='rating'),
]
