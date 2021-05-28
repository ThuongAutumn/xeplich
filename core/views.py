from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Class, Course, Room, Student
from django.views import View
import datetime

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

def get_start_and_end_day(ds_room_trong,cl):
    for i in ds_room_trong:
        if int(i.capacity) >= int(cl.number):
            cl.room = i
            d = datetime.date.today().weekday() # 0 - 6 là thứ 2 - cn
            if cl.day.find('MWF') != -1 :
                if d == 0 or d == 2 or d == 5:
                    cl.start_day = datetime.date.today() + datetime.timedelta(days=2)
                elif d == 1 or d == 3:
                    cl.start_day = datetime.date.today() + datetime.timedelta(days=1)
                else:
                    cl.start_day = datetime.date.today() + datetime.timedelta(days=3)

                dem = int(cl.course.duration)
                day = cl.start_day
                d1 = day.weekday()
                while dem > 0:
                    if d1 == 0 or d1 == 2 or d1 == 4:
                        dem -= 1
                    day += datetime.timedelta(days=1)
                    d1 = day.weekday()
                cl.end_day = day - datetime.timedelta(days=1)

            elif cl.day.find('TTS') != -1 :
                if d == 0 or d == 2 or d == 4:
                    cl.start_day = datetime.date.today() + datetime.timedelta(days=1)
                elif d == 1 or d == 3:
                    cl.start_day = datetime.date.today() + datetime.timedelta(days=2)
                else:
                    cl.start_day = datetime.date.today() + datetime.timedelta(days=3)
                
                dem = int(cl.course.duration)

                day = cl.start_day
                d1 = day.weekday()
                while dem >= 0:
                    if d1 == 1 or d1 == 3 or d1 == 5:
                        dem -= 1
                    day += datetime.timedelta(days=1)
                    d1 = day.weekday()
                cl.end_day = day- datetime.timedelta(days=1)

            else:
                if d == 5:
                    cl.start_day = datetime.date.today() + datetime.timedelta(days=2)
                else:
                    cl.start_day = datetime.date.today() + datetime.timedelta(days=1)
                
                dem = int(cl.course.duration)
                day = cl.start_day
                d1 = day.weekday()
                while dem > 0:
                    if d1 != 6:
                        dem -= 1
                    day += datetime.timedelta(days=1)
                    d1 = day.weekday()
                cl.end_day = day - datetime.timedelta(days=1)

    return cl


def xuLyXepLich(cl):
    # cl = Class.objects.get(id = 3) # bien dua vao
    rms = Room.objects.all().order_by('-capacity')

    cls_trung_day = Class.objects.filter(day = cl.day).order_by('end_day')
    print("bd xu ly")
    # kiểm tra có full phòng hay chưa
    if cls_trung_day.count() == rms.count():
        print("33, if dung")
        n = 0
        i = cls_trung_day[n]
        # tìm lớp nào sắp kết thúc và phòng chứa đủ học sinh
        # CHƯA TÍNH ĐẾN VIỆC ĐỔI PHÒNG
        while i.room.capacity < cl.number:
            n += 1
            i = cls_trung_day[n]
        cl.room = i.room
        # d = datetime.date.today().weekday() # 0 - 6 là thứ 2 - cn
        d = i.end_day.weekday()
        if cl.day.find('MWF') != -1 :
            if d == 4:
                cl.start_day = i.end_day + datetime.timedelta(days=3)
            else:
                cl.start_day = i.end_day + datetime.timedelta(days=2)
            
            dem = int(cl.course.duration)
            day = cl.start_day
            d1 = day.weekday()
            while dem > 0:
                if d1 == 0 or d1 == 2 or d1 == 4:
                    dem -= 1
                day += datetime.timedelta(days=1)
                d1 = day.weekday()
            cl.end_day = day - datetime.timedelta(days=1)

        elif cl.day.find('TTS') != -1 :
            if d == 5:
                cl.start_day = i.end_day + datetime.timedelta(days=3)
            else:
                cl.start_day = i.end_day + datetime.timedelta(days=2)
            
            dem = int(cl.course.duration)
            day = cl.start_day
            d1 = day.weekday()
            while dem > 0:
                if d1 == 1 or d1 == 3 or d1 == 5:
                    dem -= 1
                day += datetime.timedelta(days=1)
                d1 = day.weekday()
            cl.end_day = day- datetime.timedelta(days=1)

        else:
            if d == 5:
                cl.start_day = i.end_day + datetime.timedelta(days=2)
            else:
                cl.start_day = i.end_day + datetime.timedelta(days=1)
            
            dem = int(cl.course.duration)
            day = cl.start_day
            d1 = day.weekday()
            while dem > 0:
                if d1 != 6:
                    dem -= 1
                day += datetime.timedelta(days=1)
                d1 = day.weekday()
            cl.end_day = day- datetime.timedelta(days=1)
    else:
        print("45, if sai")
        dem = 0
        ds_room_trong = []
        for r in rms:
            for cls_trung in cls_trung_day:
                if cls_trung.room == r:
                    dem += 1
            if dem == 0:
                ds_room_trong.append(r)
            else:
                dem = 0

        # xếp phòng, tính startday và endday
        cl = get_start_and_end_day(ds_room_trong, cl)

    print("62,save")
    cl.status = "LOCKED"
    cl.save()
    return HttpResponse(cl.name)


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
        print("b",request)
        form = request.POST
        course = Course.objects.get(id = form['courses'])
        try:
            cl = Class.objects.create(slug = form['slug'],name = form['name'],number = form['number'], course = course, day = form['schedule'])
        except:
            return HttpResponse("lỗi thêm khoá học")
        xuLyXepLich(cl)
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
