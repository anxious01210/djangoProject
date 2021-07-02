from django import forms

from SM_app.models import CustomUser, Teacher


class CustomUserForm(forms.ModelForm):
    # user_type = forms.IntegerField(widget=forms.HiddenInput(), initial=2)

    class Meta:
        model = CustomUser
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'is_active', )
        # widgets = {'user_type': forms.HiddenInput()}
        # initial = {'user_type': 2}
        # user_type = forms.IntegerField(widget=forms.HiddenInput(), initial=2)


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        # fields = '__all__'
        fields = ('address',)
