from django.urls import path
from . import views
from .views import Classes, Courses, Rooms, Students
urlpatterns = [
    path('', views.index),
    path('classes/', Classes.as_view(),name="classes"),
    path('courses/', Courses.as_view(), name="courses"),
    path('rooms/', Rooms.as_view(), name="rooms"),
    path('students/', Students.as_view(), name="students"),
]