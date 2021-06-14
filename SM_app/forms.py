from django import forms

from SM_app.models import CustomUser, Teacher


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ('first_name', 'middle_name','last_name', 'email', 'username', 'password', 'is_active', )

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        # fields = '__all__'
        fields = ('address', )
