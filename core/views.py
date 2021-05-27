from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Class, Course, Room, Student
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
        print(request)
        return render(request, 'core/class_view.html', context)

    def post(self, request, *args, **kwargs):  
        print("b",request)
        form = request.POST
        course = Course.objects.get(id = form['courses'])
        try:
            Class.objects.create(name = form['name'],number = form['number'], course = course, day = form['schedule'])
        except:
            return HttpResponse("lỗi thêm khoá học")
        return redirect("classes")
        # return render(request, 'core/class_view.html', context)


class Courses(View):

    def get(self,request):
        courses = Course.objects.all()
        context = {
            'courses':courses
        }
        return render(request, 'core/course_view.html', context)
    
    def post(self,request,*args, **kwargs):
        form = request.POST
        try:
            Course.objects.create(name = form['name'], duration = form['duration'])
        except:
            return HttpResponse("lỗi thêm khoá học")
        return redirect("courses")


class Rooms(View):

    def get(self, request):
        rooms = Room.objects.all()
        context = {
            'rooms':rooms,
        }
        return render(request, 'core/room_view.html', context)

    def post(self, request):
        form = request.POST
        try:
            Room.objects.create(name = form['name'], capacity = form['capacity'],status=form['status'] )
        except:
            return HttpResponse("lỗi thêm khoá học")
        return redirect("rooms")


class Students(View):

    def get(self, request):
        students = Student.objects.all()
        classes = Class.objects.filter(status="WAITING")
        context = {
            'students':students,
            'classes':classes,
        }
        return render(request, 'core/student_view.html', context)

    def post(self, request):
        form = request.POST
        classes = Class.objects.filter(status="WAITING")
        
        try:
            st = Student.objects.create(name = form['name'], birth = form['birth'])
            for cl in classes:
                try:
                    s = str(cl.id)
                    value = form[s]
                    if(value != None):
                        st.classes.add(cl)
                except:
                    continue
        except:
            return HttpResponse("lỗi thêm học sinh")
        return redirect("students")
