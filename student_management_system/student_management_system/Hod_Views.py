from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Department,Academic_Year,CustomUser,Student,Staff,Subject,Semester
from django.contrib import messages

@login_required(login_url='/')
def home(request):
    return render(request, 'Hod/home.html')

@login_required(login_url='/')
def ADD_STUDENT(request):
    department = Department.objects.all()
    academic_year = Academic_Year.objects.all()

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        prn_number = request.POST.get('prn_number')
        department_id = request.POST.get('department_id')
        academic_year_id = request.POST.get('academic_year_id')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email-ID is been already in database !')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username is been already in database !')
            return redirect('add_student')
        if Student.objects.filter(prn_number=prn_number).exists():
            messages.warning(request,'PRN Number is been already in database !')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3,
            )
            user.set_password(password)
            user.save()

            department = Department.objects.get(id=department_id)
            academic_year = Academic_Year.objects.get(id=academic_year_id)

            student = Student(
                admin = user,
                prn_number = prn_number,
                gender = gender,
                date_of_birth = date_of_birth ,
                department_id = department,
                academic_year_id = academic_year,
                mobile_number = mobile_number,
            )
            student.save()
            messages.success(request, user.first_name + " " + user.last_name + " is successfully added.")
            return redirect('add_student')

    context = {
        'department':department,
        'academic_year':academic_year,
    }
    return render(request, 'Hod/add_student.html',context)


def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student':student,
    }

    return render(request,'Hod/view_student.html',context)


def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id = id)
    department =Department.objects.all()
    academic_year = Academic_Year.objects.all()

    context = {
        'student': student,
        'department' : department,
        'academic_year': academic_year,
    }
    return render(request,'Hod/edit_student.html',context)


def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        print(student_id)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        prn_number = request.POST.get('prn_number')
        department_id = request.POST.get('department_id')
        academic_year_id = request.POST.get('academic_year_id')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')

        user = CustomUser.objects.get(id = student_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin = student_id)
        if gender != None and gender != "":
            student.gender = gender
        if date_of_birth != None and date_of_birth != "":
            student.date_of_birth = date_of_birth
        student.prn_number = prn_number
        student.mobile_number = mobile_number

        department = Department.objects.get(id = department_id)
        student.department_id = department

        academic_year = Academic_Year.objects.get(id = academic_year_id)
        student.academic_year_id = academic_year

        student.save()
        messages.success(request,'Record is successfully updated !')
        return redirect('view_student')


    return render(request,'Hod/edit_student.html')


def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Record is successfully deleted !')
    return redirect('view_student')


def ADD_DEPARTMENT(request):
    if request.method == "POST":
        department_name = request.POST.get('department_name')

        department = Department(
            name = department_name,
        )
        department.save()
        messages.success(request,'Department is successfully added !')
        return redirect('add_department')

    return render(request,'Hod/add_department.html')


def VIEW_DEPARTMENT(request):
    department = Department.objects.all()

    context = {
        'department':department,
    }

    return render(request,'Hod/view_department.html',context)


def EDIT_DEPARTMENT(request,id):
    department = Department.objects.get(id = id)

    context = {
        'department': department,
    }

    return render(request,'Hod/edit_department.html',context)


def UPDATE_DEPARTMENT(request):
    if request.method == "POST":
        name = request.POST.get('department_name')
        department_id = request.POST.get('department_id')

        department = Department.objects.get(id = department_id)
        department.department_name = name
        department.save()
        messages.success(request,'Department is successfully updated !')
        return redirect('view_department')

    return render(request,'Hod/edit_department.html')


def DELETE_DEPARTMENT(request,id):
    department = Department.objects.get(id = id)
    department.delete()
    messages.success(request, 'Department is successfully deleted !')
    return redirect('view_department')


def ADD_STAFF(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email-ID is been already in database !')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username is been already in database !')
            return redirect('add_staff')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2,
            )
            user.set_password(password)
            user.save()

            staff = Staff(
                admin=user,
                gender=gender,
                mobile_number=mobile_number,
            )
            staff.save()
            messages.success(request, user.first_name + " " + user.last_name + " is successfully added.")
            return redirect('add_staff')

    return render(request,'Hod/add_staff.html')


def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff,
    }

    return render(request, 'Hod/view_staff.html', context)


def EDIT_STAFF(request,id):
    staff = Staff.objects.get(id= id)

    context = {
        'staff': staff,
    }
    return render(request, 'Hod/edit_staff.html',context )


def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        profile_pic = request.FILES.get('profile_pic')

        user = CustomUser.objects.get(id = staff_id)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin = staff_id)

        if gender != None and gender != "":
            staff.gender = gender
        staff.mobile_number = mobile_number

        staff.save()
        messages.success(request,'Record is successfully updated !')
        return redirect('view_staff')


    return render(request,'Hod/edit_staff.html')


def DELETE_STAFF(request,admin):
    staff = CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request, 'Record is successfully deleted !')
    return redirect('view_staff')


def ADD_SUBJECT(request):
    department = Department.objects.all()
    semester = Semester.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        subject_teacher = request.POST.get('subject_teacher')
        department_id = request.POST.get('department_id')
        semester_id = request.POST.get('semester_id')

        department = Department.objects.get(id = department_id)
        semester = Semester.objects.get(id = semester_id)
        staff = Staff.objects.get(id = subject_teacher)

        subject = Subject(
            name = subject_name,
            department_id = department,
            semester_id = semester,
            staff = staff,
        )
        subject.save()
        messages.success(request, 'Subject is successfully added !')
        return redirect('add_subject')

    context = {
        'department' : department,
        'semester' : semester,
        'staff' : staff
    }

    return render(request, 'Hod/add_subject.html', context)


def VIEW_SUBJECT(request):
    subject = Subject.objects.all()

    context = {
        'subject': subject,
    }

    return render(request, 'Hod/view_subject.html', context)


def EDIT_SUBJECT():
    return None


def UPDATE_SUBJECTT():
    return None


def DELETE_SUBJECT(request,staff):
    # subject = CustomUser.objects.get(id= staff)
    # subject.delete()
    # messages.success(request, 'Subject is successfully deleted !')
    # return redirect('view_subject')
    return None