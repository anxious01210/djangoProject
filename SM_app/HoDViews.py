from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from SM_app.models import CustomUser, Course, Teacher, Subject, Student
from .forms import CustomUserForm, TeacherForm


def Admin_home(request):
    return render(request, 'hod_template/home_content.html')


def add_teacher(request):
    return render(request, 'hod_template/add_teacher_template.html')


def add_teacher_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        try:
            # Manager methods¶ ==> https://docs.djangoproject.com/en/3.2/ref/contrib/auth/  -  create_user is a method already defined in django.contrib.auth AbstractUser model and objects is the model manager here.
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  first_name=first_name, last_name=last_name, user_type=2)
            user.teacher.address = address
            user.save()
            messages.success(request, 'Successfully added the Teacher.')
            return HttpResponseRedirect('/add_teacher')
        except:
            messages.error(request, 'Failed to add the Teacher.')
            return HttpResponseRedirect('/add_teacher')


def add_course(request):
    return render(request, 'hod_template/add_course_template.html')


def add_course_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed')
    else:
        course = request.POST.get('course')
        print('before try')
        try:
            course_model = Course(course_name=course)
            course_model.save()
            messages.success(request, 'Successfully added the Course.')
            return HttpResponseRedirect('/add_course')
        except:
            messages.error(request, 'Failed to add the Course.')
            return HttpResponseRedirect('/add_course')


def add_student(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'hod_template/add_student_template.html', context)


def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        course_id = request.POST.get('course')
        gender = request.POST.get('gender')

        try:
            # Manager methods¶ ==> https://docs.djangoproject.com/en/3.2/ref/contrib/auth/  -  create_user is a method already defined in django.contrib.auth AbstractUser model and objects is the model manager here.
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  first_name=first_name, last_name=last_name, user_type=3)
            user.student.address = address
            course_obj = Course.objects.get(id=course_id)
            user.student.course_id = course_obj
            user.student.session_start_year = session_start
            user.student.session_end_year = session_end
            user.student.gender = gender
            user.student.profile_pic = ''
            user.save()
            messages.success(request, 'Successfully added the Student.')
            return HttpResponseRedirect('/add_student')
        except:
            messages.error(request, 'Failed to add the Student.')
            return HttpResponseRedirect('/add_student')


def add_subject(request):
    courses = Course.objects.all()
    teachers = CustomUser.objects.filter(user_type=2)
    context = {'teachers': teachers, 'courses': courses}
    return render(request, 'hod_template/add_subject_template.html', context)


def add_subject_save(request):
    if request.method != 'POST':
        return HttpResponse('<h>Method is not allowed!</p>')
    else:
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)
        teacher_id = request.POST.get('teacher')
        teacher = CustomUser.objects.get(id=teacher_id)
        try:
            subject = Subject(course_id=course, teacher_id=teacher, subject_name=subject_name)
            subject.save()
            messages.success(request, 'Successfully Added Subject.')
            return HttpResponseRedirect('/add_subject')
        except:
            messages.error(request, 'Failed to add Subject!')
            return HttpResponseRedirect('/add_subject')


def manage_teacher(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'hod_template/manage_teacher_template.html', context)


def manage_student(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'hod_template/manage_student_template.html', context)


def manage_course(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'hod_template/manage_course_template.html', context)


def manage_subject(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'hod_template/manage_subject_template.html', context)

# def add_staff_save(request):
#     if request.method == 'POST':
#         user_form = CustomUserForm(request.POST)
#         profile_form = TeacherForm(request.POST)
#         if user_form.is_valid() and profile_form.is_valid() :
#             cd = user_form.cleaned_data
#             user = user_form.save(commit=False)
#             # user.save()
#             user.teacher.address = cd['address']
#             user.save()
#         return render(request, 'hod_template/add_staff_template_01.html', {})
#     else:
#         user_form = CustomUserForm()
#         profile_form = TeacherForm()
#         return render(request, 'hod_template/add_staff_template_01.html', {'user_form': user_form, 'profile_form': profile_form})
