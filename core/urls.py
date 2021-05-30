from django.urls import path
from . import views
from .views import Classes, Courses, Rooms, Students
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('classes/', Classes.as_view(),name="classes"),
    path('courses/', Courses.as_view(), name="courses"),
    path('rooms/', Rooms.as_view(), name="rooms"),
    path('students/', Students.as_view(), name="students"),
    path('login/',auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    # path('xuly/', views.xuLyXepLich, name="xuly"),
]