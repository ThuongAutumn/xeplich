from typing import ClassVar
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

STATUS_ROOM_CHOICES = (
    ("W", "Working"),
    ('U', 'Upgrading'),
    ('B', 'Broken')
)

DURATION_CHOICES = (
    (3, '3 Weeks' ),
    (4, '4 Weeks' ),
    (5, '5 Weeks' ),
    (6, '6 Weeks' ),
)

SCHEDULE_CHOICES = (
    ("MWF", "Shift Mon Wed Fri"),
    ("TTS", "Shift Tue Thu Sat"),
    ("F", "Shift All Week"),
)

STATUS_CHOICES = (
    ('DONE', 'Đã hoàn thành'),
    ('DOING', 'Đang học'),
    ('CANCELED', 'Đã huỷ'),
    ('WAITING', 'Đang chờ'),
    ('LOCKED', 'Đã khoá lớp'),
)
  

class Room(models.Model):
    name = models.CharField(default="", max_length=50)
    capacity = models.IntegerField(default = 0)
    status = models.CharField(choices=STATUS_ROOM_CHOICES, max_length=1, default="W")

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(default='',max_length=255)
    duration = models.IntegerField(choices=DURATION_CHOICES, default=3)

    def __str__(self):
        return self.name



class Class(models.Model):
    slug = models.SlugField(max_length=30,default='')
    name = models.CharField(default='',max_length=255)
    number = models.IntegerField(default=0)
    number_student = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courses")
    duration = models.IntegerField(default=0)
    day = models.CharField(choices=SCHEDULE_CHOICES, max_length=4) # buổi học
    status = models.CharField(choices=STATUS_CHOICES, max_length=8, default="WAITING")

    def __str__(self):
        return self.name

    

class Student(models.Model):
    name = models.CharField(default='',max_length=255)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(default='',null=True,blank=True,max_length=13)
    classes = models.ManyToManyField(Class, blank=True, null=True , related_name="students")

    def __str__(self):
        return self.name


class Week(models.Model):
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return str(self.start) + " / " + str(self.end)


class ClassRoom(models.Model):
    classID = models.ForeignKey(Class, on_delete=models.CASCADE)
    roomID = models.ForeignKey(Room, on_delete=models.CASCADE)
    weekID = models.ForeignKey(Week, on_delete=models.CASCADE)
    day = models.CharField(default="", null=True, blank=True, max_length=3)
    
    def __str__(self) -> str:
        return str(self.classID.name) + " / " + str(self.roomID.name)
    