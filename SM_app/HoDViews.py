from django.http import HttpResponse
from django.shortcuts import render
from SM_app.models import CustomUser
from .forms import CustomUserForm, TeacherForm

def Admin_home(request):
    return render(request, 'hod_template/home_content.html')


def add_staff(request):
    # return render(request, 'hod_template/add_staff_template.html')
    Full_name = Use
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        profile_form = TeacherForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid() :
            cd = user_form.cleaned_data
            cd_t = profile_form.cleaned_data
            # user = user_form.save(commit=False)
            # user.save()
            user = CustomUser.objects.create(username=cd['username'], password=cd['password'], email=cd['email'], first_name=cd['first_name'], middle_name=cd['middle_name'], last_name=cd['last_name'], user_type=2)
            user.teacher.address = cd_t['address']
            user.save()
        return HttpResponse('Teacher Added Successfully')
    else:
        user_form = CustomUserForm()
        profile_form = TeacherForm()
        return render(request, 'hod_template/add_staff_template_01.html', {'user_form': user_form, 'profile_form': profile_form})

# def add_staff_save(request):
#     if request.method != 'POST':
#         return HttpResponse('Method Not Allowed')
#     else:
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         address = request.POST.get('address')
#         user = CustomUser.objects.create(usernname=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=2)
#         user.teacher.address = address
#         user.save()

def add_staff_save(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.POST)
        profile_form = TeacherForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid() :
            cd = user_form.cleaned_data
            user = user_form.save(commit=False)
            # user.save()
            user.teacher.address = cd['address']
            user.save()
        return render(request, 'hod_template/add_staff_template_01.html', {})
    else:
        user_form = CustomUserForm()
        profile_form = TeacherForm()
        return render(request, 'hod_template/add_staff_template_01.html', {'user_form': user_form, 'profile_form': profile_form})