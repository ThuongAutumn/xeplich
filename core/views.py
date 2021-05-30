from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Class, Course, Room, Student
from django.views import View
import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    dem_so_hoc_sinh()
    cls = Class.objects.all()
    room = Room.objects.filter(status = 'W' )
    course = Course.objects.filter()
    context = {
        'classes': cls,
        'rooms': room,
        'courses': course
    }
    dem_so_hoc_sinh(cls)
    return render(request, 'core/index.html', context)

def dem_so_hoc_sinh():
    cls = Class.objects.filter(Q(status="LOCKED") | Q(status = "WAITING"))
    for cl in cls:
       cl.number_student = cl.students.all().count()
       cl.save()
    return 1

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
    print(cl.start_day)
    return cl


def xuLyXepLich(cl):
    # đưa 1 lớp (cl) mới vào xử lý return start_day, end_day và room

    rms = Room.objects.filter(status = "W").order_by('capacity') # sort tăng dần
    # những lớp cùng ca học và không có lớp nào sau khi lớp đó kết thúc
    cls_trung_ca_hoc_cuoi_cung = Class.objects.filter(day = cl.day, end = True).order_by('end_day')

    # test
    # cls_trung_day = Class.objects.all().order_by('end_day')
    # for i in cls_trung_day:
    #     print(i.end_day)
    # return HttpResponse(cls_trung_day)

    print("88 bd xu ly")
    # kiểm tra có full phòng vào thời điểm đó hay chưa

    if cls_trung_ca_hoc_cuoi_cung.count() == rms.count():
        print("33, if dung")
        # tìm lớp nào sắp kết thúc và phòng chứa đủ học sinh
        # CHƯA TÍNH ĐẾN VIỆC ĐỔI PHÒNG
        # loại trừ các lớp chưa có phòng
        n = 0
        i = cls_trung_ca_hoc_cuoi_cung[n]
        soLuongChoNgoi = i.room.capacity
        while int(soLuongChoNgoi) < int(cl.number):
            n += 1
            i = cls_trung_ca_hoc_cuoi_cung[n]
            soLuongChoNgoi = i.room.capacity

        cl.room = i.room
        i.end = False
        i.save()
        # d = datetime.date.today().weekday() # 0 - 6 là thứ 2 - cn
        d = i.end_day.weekday()
        if cl.day.find('MWF') != -1 :
            if d == 4:
                cl.start_day = i.end_day + datetime.timedelta(days=3)
            else:
                cl.start_day = i.end_day + datetime.timedelta(days=2)
            
            so_buoi_hoc = int(cl.course.duration)
            day = cl.start_day
            d1 = day.weekday()
            while so_buoi_hoc > 0:
                if d1 == 0 or d1 == 2 or d1 == 4:
                    so_buoi_hoc -= 1
                day += datetime.timedelta(days=1)
                d1 = day.weekday()
            cl.end_day = day - datetime.timedelta(days=1)

        elif cl.day.find('TTS') != -1 :
            if d == 5:
                cl.start_day = i.end_day + datetime.timedelta(days=3)
            else:
                cl.start_day = i.end_day + datetime.timedelta(days=2)
            
            so_buoi_hoc = int(cl.course.duration)
            day = cl.start_day
            d1 = day.weekday()
            while so_buoi_hoc > 0:
                if d1 == 1 or d1 == 3 or d1 == 5:
                    so_buoi_hoc -= 1
                day += datetime.timedelta(days=1)
                d1 = day.weekday()
            cl.end_day = day - datetime.timedelta(days=1)

        else:
            if d == 5:
                cl.start_day = i.end_day + datetime.timedelta(days=2)
            else:
                cl.start_day = i.end_day + datetime.timedelta(days=1)
            
            so_buoi_hoc = int(cl.course.duration)
            day = cl.start_day
            d1 = day.weekday()
            while so_buoi_hoc > 0:
                if d1 != 6:
                    so_buoi_hoc -= 1
                day += datetime.timedelta(days=1)
                d1 = day.weekday()
            cl.end_day = day - datetime.timedelta(days=1)
    else:
        print("45, if sai")
        dem = 0
        ds_room_trong = []
        for r in rms:
            for cls_trung in cls_trung_ca_hoc_cuoi_cung:
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
    cl.end = True
    cl.save()
    return HttpResponse(cl.name)


class Classes(View):

    def get(self,request):
        lop_chua_co_phong = Class.objects.filter(room = None)
        for i in lop_chua_co_phong:
            xuLyXepLich(i)
        dem_so_hoc_sinh()
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
        print(form['iId'])
        course = Course.objects.get(id = form['courses'])
        if "add_class" in form:
            try:
                cl = Class.objects.create(slug = form['slug'],name = form['name'],number = form['number'], course = course, day = form['schedule'])
                xuLyXepLich(cl)
            except:
                return HttpResponse("lỗi thêm khoá học")
        elif "update_class" in form:
            try:
                cl = Class.objects.get(pk = int(form['iId']))
                cl.slug = form['slug']
                cl.name = form['name']
                cl.number = form['number']
                cl.course = course
                cl.day = form['schedule']
                cl.save()
            except:
                return HttpResponse("Lỗi cập nhật")
        else:
            try:
                cl = Class.objects.get(pk = int(form['iId']))
                cl.delete()
                # XOÁ XONG THÌ PHẢI UPDATE LẠI PHÒNG HỌC VÀ NGÀY BĐ HỌC CÁC KHOÁ SAU NÓ NẾU CÓ
            except:
                return HttpResponse("Lỗi xoá")
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
        classes = Class.objects.filter(Q(status="LOCKED") | Q(status = "WAITING"))

        context = {
            'students':students,
            'classes':classes,
        }
        return render(request, 'core/student_view.html', context)

    def post(self, request):
        form = request.POST
        classes = Class.objects.filter(Q(status="LOCKED") | Q(status = "WAITING"))
        
        try:
            st = Student.objects.create(name = form['name'], birth = form['birth'])
            for cl in classes:
                if cl.students.all().count() < cl.room.capacity:
                    try:
                        s = str(cl.id)
                        value = form[s]
                        if(value != None):
                            st.classes.add(cl)
                    except:
                        continue
            st.save()
        except:
            return HttpResponse("lỗi thêm học sinh")
        return redirect("students")


# def a(list_l, list_r):
#     result = []
#     for j in list_l:
#         for i in list_r:
#             if result.find(i) == -1 and result.find(j) == -1:
#                 if i.cp >= j.number:
#                     j.room = i
#                     result.append({"room":i,"class":j})
#     return result

# def optimal(n, cls, rms, nc):
#     rs = a(cls,rms)
#     if len(rs) == len(cls):
#         for r in rs:
#             cl = r['class']
#             rm = r['room']
#             cl.room = rm
#             cl.save()
#     elif cls[n+1].room.capycity >= nc.number :
#         nc.room = Room.objects.get(cls[n+1].room)
#     else:
#         cl = []
#         n += 1
#         for i in range(n, len(cls)):
#             cl.append(rms[i])
#         optimal(n,cl,rms,nc)