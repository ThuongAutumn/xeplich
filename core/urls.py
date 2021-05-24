from django.urls import path
from . import views
from .views import Classes
urlpatterns = [
    path('', views.index),
    path('class/', Classes.as_view()),
]