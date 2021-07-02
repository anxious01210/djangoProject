from django.urls import path
from . import views, HoDViews

app_name = 'sm_ap'

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('', views.show_login_page, name='login'),
    path('get_user_details/', views.get_user_details, name='get_user_details'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('test/', views.test, name='test'),
    path('admin_home/', HoDViews.Admin_home, name='admin_home'),
    path('add_teacher/', HoDViews.add_teacher, name='add_teacher'),
    path('add_teacher_save/', HoDViews.add_teacher_save, name='add_teacher_save'),
    path('add_course/', HoDViews.add_course, name='add_course'),
    path('add_course_save/', HoDViews.add_course_save, name='add_course_save'),
    path('add_student/', HoDViews.add_student, name='add_student'),
    path('add_student_save/', HoDViews.add_student_save, name='add_student_save'),
    path('add_subject/', HoDViews.add_subject, name='add_subject'),
    path('add_subject_save/', HoDViews.add_subject_save, name='add_subject_save'),
    path('manage_teacher/', HoDViews.manage_teacher, name='manage_teacher'),
    path('manage_student/', HoDViews.manage_student, name='manage_student'),
    path('manage_course/', HoDViews.manage_course, name='manage_course'),
    path('manage_subject/', HoDViews.manage_subject, name='manage_subject'),
    path('edit_teacher/<str:teacher_id>/', HoDViews.edit_teacher, name='edit_teacher'), # It works with str or slug which both are string, not working with int.
    path('edit_teacher_save/', HoDViews.edit_teacher_save, name='edit_teacher_save'),
    path('edit_student/<str:student_id>/', HoDViews.edit_student, name='edit_student'), # It works with str or slug which both are string, not working with int.
    path('edit_student_save/', HoDViews.edit_student_save, name='edit_student_save'),


]

