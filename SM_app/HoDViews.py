from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from SM_app.models import CustomUser, Course, Teacher, Subject, Student
from .forms import CustomUserForm, TeacherForm, AddStudentForm, EditStudentForm


def Admin_home(request):
    return render(request, 'hod_template/home_content.html')


def add_teacher(request):
    user_form = CustomUserForm()
    profile_form = TeacherForm()
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'hod_template/add_teacher_template_01.html', context)


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
            return HttpResponseRedirect(reverse('sm_app:add_teacher'))
        except:
            messages.error(request, 'Failed to add the Teacher.')
            return HttpResponseRedirect(reverse('sm_app:add_teacher'))


#  Mehdi
# def add_teacher_save(request):
#     if request.method == 'POST':
#         user_form = CustomUserForm(request.POST)
#         profile_form = TeacherForm(request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             # user_form.cleaned_data['user_type'] = '2'
#             # cd_user_form = user_form.cleaned_data
#             # if cd_user_form['user_type']:
#             #     user_form.user_type = '2'
#             new_teacher = user_form.save(commit=False)
#             new_address = profile_form.save(commit=False)
#             new_teacher.set_password(user_form.cleaned_data['password'])
#
#             # cd = user_form.cleaned_data
#             # cd_address = profile_form.cleaned_data
#             # address = cd_address['address']
#             # user = user_form.save(commit=False)
#             # user.save()
#             # user.teacher.address = cd[address]
#             # user.save()
#             # user_form.save()
#             # profile_form.save()
#             # new_teacher.user_type = 2
#             # obj.tank = TankProfile.objects.get(pk=form.cleaned_data['tank_id'])
#             # new_teacher.user_type = 2
#             # user_form.user_type = '2'
#             # new_teacher.user_type = 2
#             new_teacher.save()
#
#             # print(new_teacher.id)
#             new_address.admin_id = new_teacher.id
#             new_address.save()
#
#             user_model = CustomUser.objects.get(id=new_teacher.id)
#             print(user_model, 'CustomUser ID is: ', new_teacher.id, 'user_type is: ', new_teacher.user_type)
#             user_model.user_type = 2
#             print(user_model, 'CustomUser ID is: ', new_teacher.id, 'user_type is: ', new_teacher.user_type)
#             # user_model.user_type = '2'
#             # print(user_model, 'CustomUser ID is: ', new_teacher.id, 'user_type is: ', new_teacher.user_type)
#             user_model.save()
#
#             messages.success(request, 'Successfully added the Teacher.')
#             return HttpResponseRedirect( '/add_teacher')
#     else:
#         user_form = CustomUserForm()
#         profile_form = TeacherForm()
#         messages.error(request, 'Failed to add the Teacher.')
#         return render(request, 'hod_template/add_teacher_template_01.html', {'user_form': user_form, 'profile_form': profile_form})


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
            return HttpResponseRedirect(reverse('sm_app:add_course'))
        except:
            messages.error(request, 'Failed to add the Course.')
            return HttpResponseRedirect(reverse('sm_app:add_course'))


def add_student(request):
    form = AddStudentForm()
    # courses = Course.objects.all()
    context = {'form': form}
    return render(request, 'hod_template/add_student_template.html', context)


def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse('Method Not Allowed')
    else:
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            first_name = cd['first_name']
            last_name = cd['last_name']
            username = cd['username']
            email = cd['email']
            password = cd['password']
            address = cd['address']
            session_start = cd['session_start']
            session_end = cd['session_end']
            course_id = cd['course']
            gender = cd['gender']

            try:
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            except:
                profile_pic = None

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
                if profile_pic is not None:
                    user.student.profile_pic = profile_pic_url
                user.save()
                messages.success(request, 'Successfully added the Student.')
                return HttpResponseRedirect(reverse('sm_app:add_student'))
            except:
                messages.error(request, 'Failed to add the Student.')
                return HttpResponseRedirect(reverse('sm_app:add_student'))
        else:
            form = AddStudentForm(request.POST)
            return render(request, 'hod_template/add_student_template.html', {'form': form})


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
            return HttpResponseRedirect(reverse('sm_app:add_subject'))
        except:
            messages.error(request, 'Failed to add Subject!')
            return HttpResponseRedirect(reverse('sm_app:add_subject'))


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
    context = {'teacher': teacher, 'id': teacher_id}
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
            return HttpResponseRedirect(reverse('sm_app:edit_teacher', kwargs={'teacher_id': teacher_id}))
        except:
            messages.error(request, 'Failed to Edit Teacher!')
            return HttpResponseRedirect(reverse('sm_app:edit_teacher', kwargs={'teacher_id': teacher_id}))


def edit_student(request, student_id):  # This student_id is actually student.admin.id
    # Before showing the form data, the student_id is stored into session in backend
    request.session['student_id'] = student_id
    student = Student.objects.get(admin=student_id)

    form = EditStudentForm()
    form.fields['email'].initial = student.admin.email  # Setting default value in form
    form.fields['first_name'].initial = student.admin.first_name  # Setting default value in form
    form.fields['last_name'].initial = student.admin.last_name  # Setting default value in form
    form.fields['username'].initial = student.admin.username  # Setting default value in form
    form.fields['address'].initial = student.address  # Setting default value in form
    form.fields['course'].initial = student.course_id.id  # Setting default value in form
    form.fields['gender'].initial = student.gender  # Setting default value in form
    form.fields['session_start'].initial = student.session_start_year  # Setting default value in form
    form.fields['session_end'].initial = student.session_end_year  # Setting default value in form
    form.fields['session_end'].initial = student.session_end_year  # Setting default value in form

    context = {'form': form, 'id': student_id, 'username': student.admin.username}
    return render(request, 'hod_template/edit_student_template.html', context)


def edit_student_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2> Method is not allowed! </h2>')
    else:
        student_id = request.session.get('student_id')
        if student_id is None:
            return HttpResponseRedirect(reverse('sm_app:manage_student'))

        form = EditStudentForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            first_name = cd['first_name']
            last_name = cd['last_name']
            username = cd['username']
            email = cd['email']
            address = cd['address']
            session_start = cd['session_start']
            session_end = cd['session_end']
            course_id = cd['course']
            gender = cd['gender']
            if request.FILES.get('profile_pic', False):  # ('File_key', Default_Value)
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

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
                if profile_pic_url is not None:
                    student.profile_pic = profile_pic_url
                student.save()
                del request.session['student_id']
                messages.success(request, 'Successfully Edited Student.')
                return HttpResponseRedirect(reverse('sm_app:edit_student', kwargs={'student_id': student_id}))
            except:
                messages.error(request, 'Failed to Edit Student!')
                return HttpResponseRedirect(reverse('sm_app:edit_student', kwargs={'student_id': student_id}))
        else:
            form = EditStudentForm(request.POST)
            student = Student.objects.get(admin=student_id)
            context = {'form': form, 'id': student_id, 'username': student.admin.username}
            return render(request, 'hod_template/edit_student_template.html', context)


def edit_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    courses = Course.objects.all()
    # teachers = Teacher.objects.filter(admin__user_type = 2)
    teachers = CustomUser.objects.filter(user_type=2)
    context = {'subject': subject, 'courses': courses, 'teachers': teachers, 'id': subject_id}
    return render(request, 'hod_template/edit_subject_template.html', context)


def edit_subject_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2> Method is not allowed! </h2>')
    else:
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        teacher_id = request.POST.get('teacher')
        course_id = request.POST.get('course')
        try:
            subject = Subject.objects.get(id=subject_id)
            subject.subject_name = subject_name
            teacher = CustomUser.objects.get(id=teacher_id)
            subject.teacher_id = teacher
            course = Course.objects.get(id=course_id)
            subject.course_id = course
            subject.save()
            messages.success(request, 'Successfully Edited Subject.')
            # return HttpResponseRedirect('edit_subject/' + subject_id)
            return HttpResponseRedirect(reverse('sm_app:edit_subject', kwargs={'subject_id': subject_id}))
        except:
            messages.error(request, 'Failed to Edit Subject!')
            # return HttpResponseRedirect('/edit_subject/' + subject_id)
            # return HttpResponseRedirect(reverse('sm_app:edit_subject', subject_id))  # We can pass data in reverse with kwarg={'URL_PARAM': 'VALUE'}
            return HttpResponseRedirect(reverse('sm_app:edit_subject', kwargs={'subject_id': subject_id}))


def edit_course(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {'course': course, 'id': course_id}
    return render(request, 'hod_template/edit_course_template.html', context)


def edit_course_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2> Method is not allowed! </h2>')
    else:
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course')
        try:
            course = Course.objects.get(id=course_id)
            course.course_name = course_name
            course.save()
            messages.success(request, 'Successfully Edited Course.')
            return HttpResponseRedirect(reverse('sm_app:edit_course', kwargs={'course_id': course_id}))
        except:
            messages.error(request, 'Failed to Edit Course!')
            return HttpResponseRedirect(reverse('sm_app:edit_course', kwargs={'course_id': course_id}))

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
