from django.contrib import admin
from .models import Room, Class, Course, Student, Week, ClassRoom
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth', 'phone']

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity', 'status']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration']

class WeekAdmin(admin.ModelAdmin):
    list_display = ['start', 'end']

class ClassRoomAdmin(admin.ModelAdmin):
    list_display = [
        "classID",
        "roomID",
        "weekID",
        "day",
    ]

class ClassAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'number', 'day', 'course', 'status' ,'duration']


admin.site.register(Student, StudentAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register( ClassRoom, ClassRoomAdmin)


