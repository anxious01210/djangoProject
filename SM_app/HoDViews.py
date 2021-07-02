from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from SM_app.models import CustomUser, Course, Teacher, Subject, Student
from .forms import CustomUserForm, TeacherForm


def Admin_home(request):
    return render(request, 'hod_template/home_content.html')


def add_teacher(request):
    user_form = CustomUserForm()
    profile_form = TeacherForm()
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'hod_template/add_teacher_template_01.html', context)


# def add_teacher_save(request):
#     if request.method != 'POST':
#         return HttpResponse('Method Not Allowed')
#     else:
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         address = request.POST.get('address')
#         try:
#             # Manager methods¶ ==> https://docs.djangoproject.com/en/3.2/ref/contrib/auth/  -  create_user is a method already defined in django.contrib.auth AbstractUser model and objects is the model manager here.
#             user = CustomUser.objects.create_user(username=username, password=password, email=email,
#                                                   first_name=first_name, last_name=last_name, user_type=2)
#             user.teacher.address = address
#             user.save()
#             messages.success(request, 'Successfully added the Teacher.')
#             return HttpResponseRedirect('/add_teacher')
#         except:
#             messages.error(request, 'Failed to add the Teacher.')
#             return HttpResponseRedirect('/add_teacher')


def add_teacher_save(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        profile_form = TeacherForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # user_form.cleaned_data['user_type'] = '2'
            # cd_user_form = user_form.cleaned_data
            # if cd_user_form['user_type']:
            #     user_form.user_type = '2'
            new_teacher = user_form.save(commit=False)
            new_address = profile_form.save(commit=False)
            new_teacher.set_password(user_form.cleaned_data['password'])

            # cd = user_form.cleaned_data
            # cd_address = profile_form.cleaned_data
            # address = cd_address['address']
            # user = user_form.save(commit=False)
            # user.save()
            # user.teacher.address = cd[address]
            # user.save()
            # user_form.save()
            # profile_form.save()
            # new_teacher.user_type = 2
            # obj.tank = TankProfile.objects.get(pk=form.cleaned_data['tank_id'])
            # new_teacher.user_type = 2
            # user_form.user_type = '2'
            # new_teacher.user_type = 2
            new_teacher.save()

            # print(new_teacher.id)
            new_address.admin_id = new_teacher.id
            new_address.save()

            user_model = CustomUser.objects.get(id=new_teacher.id)
            print(user_model, 'CustomUser ID is: ', new_teacher.id, 'user_type is: ', new_teacher.user_type)
            user_model.user_type = 2
            print(user_model, 'CustomUser ID is: ', new_teacher.id, 'user_type is: ', new_teacher.user_type)
            # user_model.user_type = '2'
            # print(user_model, 'CustomUser ID is: ', new_teacher.id, 'user_type is: ', new_teacher.user_type)
            user_model.save()

            messages.success(request, 'Successfully added the Teacher.')
            return HttpResponseRedirect( '/add_teacher')
    else:
        user_form = CustomUserForm()
        profile_form = TeacherForm()
        messages.error(request, 'Failed to add the Teacher.')
        return render(request, 'hod_template/add_teacher_template_01.html', {'user_form': user_form, 'profile_form': profile_form})


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


def edit_teacher(request, teacher_id):
    # return HttpResponse('Teacher ID: ' + teacher_id)
    teacher = Teacher.objects.get(admin=teacher_id)
    context = {'teacher': teacher}
    return render(request, 'hod_template/edit_teacher_template.html', context)


def edit_teacher_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method Not Allowed</h2>')
    else:
        teacher_id = request.POST.get('teacher_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.get(id=teacher_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()

            teacher_model = Teacher.objects.get(admin=teacher_id)
            teacher_model.address = address
            teacher_model.save()
            messages.success(request, 'Successfully Edited Teacher.')
            return HttpResponseRedirect('/edit_teacher/' + teacher_id)
        except:
            messages.error(request, 'Failed to Edit Teacher!')
            return HttpResponseRedirect('/edit_teacher' + teacher_id)


def edit_student(request, student_id):  # This student_id is actually student.admin.id
    courses = Course.objects.all()
    student = Student.objects.get(admin=student_id)
    context = {'courses': courses, 'student': student}
    return render(request, 'hod_template/edit_student_template.html', context)

def edit_student_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2> Method is not allowed! </h2>')
    else:
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        course_id = request.POST.get('course')
        gender = request.POST.get('gender')
        try:
            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

            student = Student.objects.get(admin=student_id)
            student.address = address
            student.session_start_year = session_start
            student.session_end_year = session_end
            student.gender = gender

            course = Course.objects.get(id=course_id)
            student.course_id = course
            student.save()
            messages.success(request, 'Successfully Edited Student.')
            return HttpResponseRedirect('/edit_student/' + student_id)
        except:
            messages.error(request, 'Failed to Edit Student!')
            return HttpResponseRedirect('/edit_student/' + student_id)




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
