from django.core import exceptions
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Class, Course, Room, Student, Week, ClassRoom
from django.views import View
import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .forms import RegistrationForm

# region Front handler

def towf(rms, cls):
    list_cac_th = []
    list_max = []
    try:
        for i in range(rms.count()):
            if rms[i].capacity >= cls[0].number:
                for j in range(rms.count()):
                    if rms[j].capacity >= cls[1].number:
                        list_cach = [
                            [i,cls[0].duration],
                            [j,cls[1].duration],
                        ]
                        tong = 0
                        max = 0
                        for o in range(rms.count()): # tính max tổng duration
                            for p in list_cach:
                                if o == p[0]:
                                    tong += p[1]
                            if max < tong:
                                max = tong
                            tong = 0
                        list_max.append(max)
                        list_cac_th.append([list_cach,max])
    except:
        print("lỗi towf()")
    return list_cac_th, list_max

def threef(rms, cls): # i j k l m
    list_cac_th = []
    list_max = []
    try:
        for i in range(rms.count()):
            if rms[i].capacity >= cls[0].number:
                for j in range(rms.count()):
                    if rms[j].capacity >= cls[1].number:
                        for k in range(rms.count()):
                            if rms[k].capacity >= cls[2].number:          
                                list_cach = [
                                    [i,cls[0].duration],
                                    [j,cls[1].duration],
                                    [k,cls[2].duration],
                                ]
                                tong = 0
                                max = 0
                                for o in range(rms.count()): # tính max tổng duration
                                    for p in list_cach:
                                        if o == p[0]:
                                            tong += p[1]
                                    if max < tong:
                                        max = tong
                                    tong = 0
                                list_max.append(max)
                                list_cac_th.append([list_cach,max])

    except:
        print("lỗi threef()")
    return list_cac_th, list_max

def fourf(rms, cls): # i j k l m
    list_cac_th = []
    list_max = []
    try:
        for i in range(rms.count()):
            if rms[i].capacity >= cls[0].number:
                for j in range(rms.count()):
                    if rms[j].capacity >= cls[1].number:
                        for k in range(rms.count()):
                            if rms[k].capacity >= cls[2].number:
                                for l in range(rms.count()):
                                    if rms[l].capacity >= cls[3].number:
                                        list_cach = [
                                            [i,cls[0].duration],
                                            [j,cls[1].duration],
                                            [k,cls[2].duration],
                                            [l,cls[3].duration],
                                        ]
                                        tong = 0
                                        max = 0
                                        for o in range(rms.count()): # tính max tổng duration
                                            for p in list_cach:
                                                if o == p[0]:
                                                    tong += p[1]
                                            if max < tong:
                                                max = tong
                                            tong = 0
                                        list_max.append(max)
                                        list_cac_th.append([list_cach,max])
    except:
        print("lỗi fourf()")
    return list_cac_th, list_max

def fivef(rms, cls): # i j k l m
    list_cac_th = []
    list_max = []
    try:
        for i in range(rms.count()):
            if rms[i].capacity >= cls[0].number:
                for j in range(rms.count()):
                    if rms[j].capacity >= cls[1].number:
                        for k in range(rms.count()):
                            if rms[k].capacity >= cls[2].number:
                                for l in range(rms.count()):
                                    if rms[l].capacity >= cls[3].number:
                                        for m in range(rms.count()):
                                            if rms[m].capacity >= cls[4].number:
                                                list_cach = [
                                                    [i,cls[0].duration],
                                                    [j,cls[1].duration],
                                                    [k,cls[2].duration],
                                                    [l,cls[3].duration],
                                                    [m,cls[4].duration],
                                                ]
                                                tong = 0
                                                max = 0
                                                for o in range(rms.count()): # tính max tổng duration
                                                    for p in list_cach:
                                                        if o == p[0]:
                                                            tong += p[1]
                                                    if max < tong:
                                                        max = tong
                                                    tong = 0
                                                list_max.append(max)
                                                list_cac_th.append([list_cach,max])
    except:
        print("lỗi fivef()")
    return list_cac_th, list_max

#list_cac_th, list_max
def sixf(rms, cls): # i j k l m
    list_cac_th = []
    list_max = []
    try:
        for i in range(rms.count()):
            if rms[i].capacity >= cls[0].number:
                for j in range(rms.count()):
                    if rms[j].capacity >= cls[1].number:
                        for k in range(rms.count()):
                            if rms[k].capacity >= cls[2].number:
                                for l in range(rms.count()):
                                    if rms[l].capacity >= cls[3].number:
                                        for m in range(rms.count()):
                                            if rms[m].capacity >= cls[4].number:
                                                for n in range(rms.count()):
                                                    if rms[n].capacity >= cls[4].number:

                                                        list_cach = [
                                                            [i,cls[0].duration],
                                                            [j,cls[1].duration],
                                                            [k,cls[2].duration],
                                                            [l,cls[3].duration],
                                                            [m,cls[4].duration],
                                                            [n,cls[5].duration],
                                                        ]
                                                        tong = 0
                                                        max = 0
                                                        for o in range(rms.count()): # tính max tổng duration
                                                            for p in list_cach:
                                                                if o == p[0]:
                                                                    tong += p[1]
                                                            if max < tong:
                                                                max = tong
                                                            tong = 0
                                                        list_max.append(max)
                                                        list_cac_th.append([list_cach,max])
    except:
        print("lỗi sixf()")
    return list_cac_th, list_max

def case(n, rms, cls):
    switcher = {
        2 : towf(rms, cls),
        3 : threef(rms, cls),
        4 : fourf(rms, cls),
        5 : fivef(rms, cls),
        6 : sixf(rms, cls)
    }
    return switcher.get(n,"nothing")

#for5 cũ
def xuly246357(rms, cls): # i j k l m
    result = case(cls.count(),rms,cls)
    list_cac_th = result[0]
    list_max = result[1]
    
    m = min(list_max)
    for i in list_cac_th:
        if i[1] == m:
            truong_hop_chon = i[0]
            print( "cach xep phong :",i[0])
            # tách ds index phòng
            list_index_room = []
            list_index_duration = []


            for j in range(len(i[0])):
                rm = rms[i[0][j][0]]
                cl =  cls[j]
                today = datetime.date.today() # .day.weekday() # thứ 2 -> cn = 0 -> 6
                dtt = datetime.timedelta(days= 7 * i[0][j][1] ) # delta time

                if list_index_room.count(i[0][j][0]) == 0:
                    list_index_room.append(i[0][j][0])
                    list_index_duration.append(i[0][j][1])
                    weeks = Week.objects.filter(Q(start__lt = today + dtt) & Q(start__gt = today) ).order_by("-end") # giảm dần
                    for w in weeks:
                        clrm, created = ClassRoom.objects.get_or_create(
                            weekID = w,
                            roomID = rm,
                            classID = cl,
                            defaults={
                                "day" :cl.day
                            }
                        )
                else:
                    dem = 0
                    for l in range(len(list_index_room)):
                        if list_index_room[l] == i[0][j][0]:
                            dem += list_index_duration[l]
                  
                    list_index_room.append(i[0][j][0])
                    list_index_duration.append(i[0][j][1])
                    today = datetime.date.today() # .day.weekday() # thứ 2 -> cn = 0 -> 6
                    dtt = datetime.timedelta(days= 7 * dem ) # delta time
                    weeks = Week.objects.filter(Q(start__gt = today + dtt) & Q(start__lt = today + dtt + datetime.timedelta(days= 7 * i[0][j][1] )) ).order_by("-end") # giảm dần
                    for w in weeks:
                        clrm, created = ClassRoom.objects.get_or_create(
                            weekID = w,
                            roomID = rm,
                            classID = cl,
                            defaults={
                                "day" :cl.day
                            }
                        )

            break

    return truong_hop_chon


def for6(rms, cls): # i j k l m
    list_cac_th = []
    list_max = []
    for i in range(rms.count()):
        if rms[i].capacity >= cls[0].number:
            for j in range(rms.count()):
                if rms[j].capacity >= cls[1].number:
                    for k in range(rms.count()):
                        if rms[k].capacity >= cls[2].number:
                            for l in range(rms.count()):
                                if rms[l].capacity >= cls[3].number:
                                    for m in range(rms.count()):
                                        if rms[m].capacity >= cls[4].number:
                                            for n in range(rms.count()):
                                                if rms[n].capacity >= cls[4].number:

                                                    list_cach = [
                                                        [i,cls[0].duration],
                                                        [j,cls[1].duration],
                                                        [k,cls[2].duration],
                                                        [l,cls[3].duration],
                                                        [m,cls[4].duration],
                                                        [n,cls[5].duration],
                                                    ]
                                                    tong = 0
                                                    max = 0
                                                    for o in range(rms.count()): # tính max tổng duration
                                                        for p in list_cach:
                                                            if o == p[0]:
                                                                tong += p[1]
                                                        if max < tong:
                                                            max = tong
                                                        tong = 0
                                                    list_max.append(max)
                                                    list_cac_th.append([list_cach,max])

    m = min(list_max)
    for i in list_cac_th:
        if i[1] == m:
            truong_hop_chon = i[0]
          
            # tách ds index phòng
            list_index_room = []
            list_index_duration = []


            for j in range(len(i[0])):
                rm = rms[i[0][j][0]]
                cl =  cls[j]
                today = datetime.date.today() # .day.weekday() # thứ 2 -> cn = 0 -> 6
                dtt = datetime.timedelta(days= 7 * i[0][j][1] ) # delta time

                if list_index_room.count(i[0][j][0]) == 0:
                    list_index_room.append(i[0][j][0])
                    list_index_duration.append(i[0][j][1])
                    weeks = Week.objects.filter(Q(start__lt = today + dtt) & Q(start__gt = today) ).order_by("-end") # giảm dần
                    for w in weeks:
                        clrm, created = ClassRoom.objects.get_or_create(
                            weekID = w,
                            roomID = rm,
                            classID = cl,
                            defaults={
                                "day" :cl.day
                            }
                        )
                else:
                    dem = 0
                    for l in range(len(list_index_room)):
                        if list_index_room[l] == i[0][j][0]:
                            dem += list_index_duration[l]
                  
                    list_index_room.append(i[0][j][0])
                    list_index_duration.append(i[0][j][1])
                    today = datetime.date.today() # .day.weekday() # thứ 2 -> cn = 0 -> 6
                    dtt = datetime.timedelta(days= 7 * dem ) # delta time
                    weeks = Week.objects.filter(Q(start__gt = today + dtt) & Q(start__lt = today + dtt + datetime.timedelta(days= 7 * i[0][j][1] )) ).order_by("-end") # giảm dần
                    for w in weeks:
                        clrm, created = ClassRoom.objects.get_or_create(
                            weekID = w,
                            roomID = rm,
                            classID = cl,
                            defaults={
                                "day" :cl.day
                            }
                        )

            break
    return truong_hop_chon

# index phòng và giá trị thời lượng học min
def tim_thoi_luong_hoc_min(list_cac_th,cls):

    rms = Room.objects.filter(status = 'W' ).order_by("capacity") # tăng dần
    list_tong_tg = []
    for j in range(rms.count()):
        tong_tg = 0
        for i in list_cac_th: # [[[index_room, thoigiancho]], tong thoi gian cho]
            if int(i[0]) == j:
                tong_tg += int(i[1])
        list_tong_tg.append(tong_tg)


    index_min = -1
    min = 1000
    # index_min = 0
    # min = list_tong_tg[index_min]
    for i in range(len(list_tong_tg)):
        if list_tong_tg[i] < min and cls.number <= rms[i].capacity:
            print("so hs va so cho ngoi :",cls.number, " va ",rms[i].capacity)
            min = list_tong_tg[i]
            index_min = i
    print("index_min, min :",index_min, min)
    return index_min, min


# xếp lớp full tuần
def xulyfullweek():
    rms = Room.objects.filter(status = 'W' ).order_by("capacity") # tăng dần

    cls1 = Class.objects.filter(day = "MWF").order_by("duration")
    cls2 = Class.objects.filter(day = "TTS").order_by("duration")
    cls3 = Class.objects.filter(day="F").order_by("duration")

    list_th1 = []
    list_th2 = []

    print("===========")
    print("dem so lop 2 4 6: ",cls1.count())
    print("dem so lop 3 5 7: ",cls2.count())
    print("===========")
    
    list_th1 = xuly246357(rms,cls1)
    list_th2 = xuly246357(rms,cls2)

    print("truong hop xep lop 2 6 4 ",list_th1)
    print("truong hop xep lop 3 5 7 ",list_th2)
    
    if cls3.count() == 1:
        time1 = tim_thoi_luong_hoc_min(list_th1,cls3[0]) # [index_room1, waiting]
        time2 = tim_thoi_luong_hoc_min(list_th2,cls3[0]) # [index_room2, waiting]

        print("(2 4 6)[phong hoc, thoi gian cho] :" ,time1)
        print("(3 5 7)[phong hoc, thoi gian cho] :" ,time2)

        if time1[1] < time2[1]:
            waiting = time2[1] 
        else:
            waiting = time1[1]

        room_index1 = time1[0] 
        room_index2 = time2[0] 

        print("=========")
        print("index room :" ,rms[room_index1], " và ",rms[room_index2])
        print("số tuần chờ : ", waiting)
        print("=========")

        today = datetime.date.today() # .day.weekday() # thứ 2 -> cn = 0 -> 6
        dtt = datetime.timedelta(days = 7 * waiting ) # delta time
        weeks = Week.objects.filter(Q(start__gt = today + dtt) & Q(start__lt = today + dtt + datetime.timedelta(days= 7 * int(cls3[0].duration) )) ).order_by("-end") # giảm dần
        for w in weeks:
            ClassRoom.objects.get_or_create(classID = cls3[0], roomID = rms[room_index1], weekID = w, day = "MWF")
            ClassRoom.objects.get_or_create(classID = cls3[0], roomID = rms[room_index2], weekID = w, day = "TTS")
    

# endregion



# Create your views here.
@login_required
def index(request):
    current_user = request.user
    if current_user.is_staff:
        room = Room.objects.filter(status = 'W' ) # tăng dần
        cls = Class.objects.all().order_by("duration")
        course = Course.objects.filter()
        clrms = ClassRoom.objects.all()
        context = {
            'classes': cls,
            'rooms': room,
            'courses': course,
            'clrms': clrms,
        }
        return render(request, 'core/dashboard.html', context)
    else:
        return student_view(request)


@login_required
def student_view(request):
    current_user = request.user
    if current_user.is_staff == True:
        return redirect('index')
    student = Student.objects.get(user = current_user)
    rooms = Room.objects.filter(status = 'W' )
    clrms = []
    for cl in student.classes.all():
        clrm = ClassRoom.objects.filter(classID = cl)
        for j in clrm:
            clrms.append(j)
    context = {
        'rooms': rooms,
        'student':student,
        'clrms': clrms,
    }
    return render(request, 'core/student_index.html', context)



def dem_so_hoc_sinh():
    cls = Class.objects.filter(Q(status="LOCKED") | Q(status = "WAITING"))
    for cl in cls:
       cl.number_student = cl.students.all().count()
       cl.save()
    return 1


def detail_class(request, pk):
    cl = Class.objects.get(pk = pk)
    stds = cl.students.all()
    context = {
        'class':cl,
        'students':stds,
    }
    return render(request, 'core/detail_class.html', context)

@method_decorator(login_required(), name='dispatch')
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
        form = request.POST
        course = Course.objects.get(id = form['courses'])
        duration = course.duration
        if "add_class" in form:
            try:
                cl = Class.objects.create(slug = form['slug'],name = form['name'],number = form['number'], course = course, day = form['schedule'], duration = duration)
                messages.success(request,"Thêm lớp học thành công!")
            except:
                messages.warning(request,"Lỗi thêm lớp học!")
                return redirect("classes")
        elif "update_class" in form:
            try:
                cl = Class.objects.get(pk = int(form['iId']))
                cl.slug = form['slug']
                cl.name = form['name']
                cl.number = form['number']
                cl.course = course
                cl.day = form['schedule']
                cl.save()
                messages.success(request,"Cập nhật lớp học thành công!")
            except:
                messages.warning(request,"Lỗi cập nhật lớp học!")
                return redirect("classes")
        else:
            try:
                cl = Class.objects.get(pk = int(form['iId']))
                cl.delete()
                messages.success(request,"Xoá lớp học thành công!")
                # XOÁ XONG THÌ PHẢI UPDATE LẠI PHÒNG HỌC VÀ NGÀY BĐ HỌC CÁC KHOÁ SAU NÓ NẾU CÓ
            except:
                messages.Warning(request,"Lỗi xoá lớp học!")
                return redirect("classes")
        
        clrms = ClassRoom.objects.all().delete()
        # dem_so_hoc_sinh()
        xulyfullweek()
        return redirect("classes")
        # return render(request, 'core/class_view.html', context)

@method_decorator(login_required(), name='dispatch')
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
            messages.success(request,"Thêm khoá học thành công!")
        except:
            messages.warning(request,"Lỗi thêm khoá học!")
        return redirect("courses")

def DeleteCourse(request,pk):
    Course.objects.get(pk = pk).delete()
    messages.success(request,"Xoá khoá học thành công!")
    return redirect("courses")

@method_decorator(login_required(), name='dispatch')
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
            messages.success(request,"Thêm phòng thành công!")
        except:
            messages.warning(request,"lỗi thêm phòng học!")
        return redirect("rooms")


def DeleteRoom(request,pk):
    Room.objects.get(pk = pk).delete()
    messages.success(request,"Xoá phòng thành công!")
    return redirect("rooms")


@method_decorator(login_required(), name='dispatch')
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

        list_lop_day = []
        flag_phong_day = False
        if 'add_student' in form:
            messages.warning(request,"Bạn không thể thêm!")
            return redirect("students")
            try:
                st = Student.objects.create(name = form['name'], birth = form['birth'])
                for cl in classes:
                    print("count ",cl.students.all().count())
                    if cl.students.all().count() <= cl.number:
                        try:
                            s = str(cl.id)
                            value = form[s]
                            if(value != None):
                                st.classes.add(cl)
                                if cl.students.all().count() > cl.number:
                                    cl.number = cl.students.all().count()
                                    cl.save()
                        except:
                            continue
                    else:
                        flag_phong_day = True
                        list_lop_day.append(cl.slug)
                st.save()
            except:
                return HttpResponse("lỗi thêm học sinh")
            if flag_phong_day == True:
                text = ''
                for i in list_lop_day:
                    text += ', '+i
                return HttpResponse("phòng của lớp ", text , ' đã đầy')

        elif 'update_student' in form:
            try:
                std = Student.objects.get(id = form['sId'])
                std.name = form['name']
                std.birth = form['birth']
                # reset class.number_student
                for cl in std.classes.all():
                    cl.number_student -= 1
                    cl.save()
                # add new classes in student
                std.classes.clear()
                for cl in classes:
                    clrm = ClassRoom.objects.filter(classID = cl.id)
                    if cl.students.all().count() < clrm[0].roomID.capacity:
                        print("Phòng còn chỗ")
                        try:
                            s = str(cl.id)
                            value = form.get(s,None)
                            if(value != None):
                                std.classes.add(cl)
                                std.save()
                                print("thêm lớp thành công", cl.number_student)
                                cl.number_student += 1
                                print("số hs :", cl.number_student)
                                cl.save()
                                if cl.students.all().count() > cl.number:
                                    cl.number = cl.students.all().count()
                                    cl.save()
                            else:
                                print("ID lớp None")
                        except:
                            print("không get được id")
                    else:
                        flag_phong_day = True
                        list_lop_day.append(cl.slug)
                messages.success(request,"Cập nhật học sinh thành công!")
            except:
                messages.warning(request,"Lỗi cập nhật học sinh")
                return redirect("students")
            if flag_phong_day == True:
                text = ''
                for i in list_lop_day:
                    text += ', '+i
                messages.warning(request,"phòng của lớp ", text , ' đã đầy')
                return redirect("students")
        # xoá học sinh
        else:
            try:
                messages.warning(request,"Không thể xoá!")
                # Student.objects.get(id = form['sId']).delete()
            except:
                messages.warning(request,"Không thể xoá!")

        return redirect("students")



def register(request):
    form =RegistrationForm()
    if request.method =='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'core/register.html',{'form':form})

@login_required
def Profiles(request):
    current_user = request.user
    if current_user.is_staff:
        # messages.Info(request,"You are admin!")
        return redirect('index')
    student = Student.objects.get(user = current_user)
    cls = student.classes.all()
    context = {
        'student':student,
        'cls':cls,
    }
    return render(request, 'core/profile.html',context)

@login_required    
def UpdateProfile(request):
    current_user = request.user
    form = request.POST
    name = form.get("name",None)
    birth = form.get("birth",None)
    phone = form.get("phone",None)
    if name != None:
        std = Student.objects.get(user = current_user)
        std.name = name
        std.birth = birth
        std.phone = phone
        std.save()
    else:
        return HttpResponse("lỗi")
    return redirect('profile')

