from django import forms
from django.utils.translation import gettext as _
from SM_app.models import CustomUser, Teacher, Course


class CustomUserForm(forms.ModelForm):
    # user_type = forms.IntegerField(widget=forms.HiddenInput(), initial=2)

    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'is_active',)
        # widgets = {'user_type': forms.HiddenInput()}
        # initial = {'user_type': 2}
        # user_type = forms.IntegerField(widget=forms.HiddenInput(), initial=2)


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        # fields = '__all__'
        fields = ('address',)


class DataInput(forms.DateInput):
    input_type = 'Date'


class AddStudentForm(forms.Form):
    # email = forms.EmailInput(label='Email',attrs={'placeholder': _('Email')})
    email = forms.EmailField(label='Email', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    courses = Course.objects.all()
    course_list = []
    for course in courses:
        small_course = (course.id, course.course_name)
        course_list.append(small_course)

    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    course = forms.ChoiceField(label='Course', choices=course_list, widget=forms.Select(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label='Gender', choices=gender_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    session_start = forms.DateField(label='Session Start', widget=DataInput(attrs={'class': 'form-control'}))
    session_end = forms.DateField(label='Session End', widget=DataInput(attrs={'class': 'form-control'}))
    profile_pic = forms.FileField(label='Profile Pic', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))


class EditStudentForm(forms.Form):
    # email = forms.EmailInput(label='Email',attrs={'placeholder': _('Email')})
    email = forms.EmailField(label='Email', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    courses = Course.objects.all()
    course_list = []
    for course in courses:
        small_course = (course.id, course.course_name)
        course_list.append(small_course)

    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    course = forms.ChoiceField(label='Course', choices=course_list, widget=forms.Select(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label='Gender', choices=gender_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    session_start = forms.DateField(label='Session Start', widget=DataInput(attrs={'class': 'form-control'}))
    session_end = forms.DateField(label='Session End', widget=DataInput(attrs={'class': 'form-control'}))
    profile_pic = forms.FileField(label='Profile Pic', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))