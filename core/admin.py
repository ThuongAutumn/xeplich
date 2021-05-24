from django.contrib import admin
from .models import Room, Class, Course
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity', 'status']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration']

class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'room', 'number', 'day', 'course', 'status' ,'start_day']


admin.site.register(Room, RoomAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Class, ClassAdmin)
