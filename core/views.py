from django.shortcuts import render
from django.http import HttpResponse
from .models import Class, Course, Room 
from django.views import View

# Create your views here.

def index(request):
    cl = Class.objects.all()
    room = Room.objects.filter(status = 'W' )
    course = Course.objects.filter()
    context = {
        'classes': cl,
        'rooms': room,
        'courses': course
    }
    return render(request, 'core/index.html', context)


class Classes(View):

    def get(self,request):
        cl = Class.objects.all()
        course = Course.objects.filter()
        context = {
            'classes': cl,
            'courses': course,
        }
        return render(request, 'core/class_view.html', context)

    def post(self, request, *args, **kwargs):
        cl = Class.objects.all()
        courses = Course.objects.filter()
        
        form = request.POST
        course = Course.objects.get(id = form['courses'])
        print(form['name'])
        Class.objects.create(name = form['name'],number = form['number'], course = course, day = form['schedule'])
        context = {
            'classes': cl,
            'courses': courses,
        }

        return render(request, 'core/class_view.html', context)
