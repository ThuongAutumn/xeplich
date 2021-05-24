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
    ('2', 'Two Week'),
    ('3', 'Three Week'),
)

SCHEDULE_CHOICES = (
    ("1MWF", "Shift 1 Mon Wed Fri"),
    ("2MWF", "Shift 2 Mon Wed Fri"),
    ("1TTS", "Shift 1 Tue Thu Sat"),
    ("2TTS", "Shift 2 Tue Thu Sat"),
    ("1F", "Shift 1 All Week"),
    ("2F", "Shift 2 All Week"),
)

STATUS_CHOICES = (
    ('DONE', 'Đã hoàn thành'),
    ('DOING', 'Đang học'),
    ('CANCELED', 'Đã huỷ'),
    ('WAITING', 'Đang chờ'),
)
  

class Room(models.Model):
    name = models.CharField(default="", max_length=50)
    capacity = models.IntegerField(default = 0)
    status = models.CharField(choices=STATUS_ROOM_CHOICES, max_length=1)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(default='',max_length=255)
    duration = models.CharField(choices=DURATION_CHOICES, max_length=1)

    def __str__(self):
        return self.name


# class Schedule(models.Model):
#     day = models.CharField(choices=SCHEDULE_CHOICES, max_length=4)

#     def __str__(self):
#         return self.day

class Class(models.Model):
    name = models.CharField(default='',max_length=255)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL , null=True, blank=True)
    number = models.IntegerField(default=0)
    # schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_day = models.DateField(null=True, blank=True)
    end_day = models.DateField(null=True, blank=True)
    day = models.CharField(choices=SCHEDULE_CHOICES, max_length=4)
    status = models.CharField(choices=STATUS_CHOICES, max_length=8, default="WAITING")

    def __str__(self):
        return self.name

    def get_value_display(self):
        return self.status
