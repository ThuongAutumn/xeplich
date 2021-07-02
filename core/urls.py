from django.urls import path
from . import views
from .views import Classes, Courses, Rooms, Students
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('classes/', Classes.as_view(),name="classes"),
    path('courses/', Courses.as_view(), name="courses"),
    path('deletecourses/<int:pk>/', views.DeleteCourse, name="deletecourses"),
    path('rooms/', Rooms.as_view(), name="rooms"),
    path('deleterooms/<int:pk>/', views.DeleteRoom, name="deleterooms"),
    path('students/', Students.as_view(), name="students"),
    path('accounts/login/',auth_views.LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
    path('class/<int:pk>/', views.detail_class, name="detail_class"),
    path('register/', views.register , name='register'),
    path('profile/', views.Profiles , name='profile'),
    path('profile/update/', views.UpdateProfile , name='updateprofile'),

]