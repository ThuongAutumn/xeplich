from django.contrib import admin
from .models import Room, Class, Course, Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth']

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity', 'status']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration']

class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'room', 'number', 'day', 'course', 'status' ,'start_day', 'end']


admin.site.register(Student, StudentAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Class, ClassAdmin)
