from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

# Overriding the Default Django Auth User and adding One More Field (user_type)
class CustomUser(AbstractUser):
    """Django data model CustomUser"""
    user_type_data = ((1, 'HOD'), (2, 'Teacher'), (3, 'Student'), (4, 'Parent'), (5, 'Staff'), (6, 'SemiAdmin'),)
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class Parent(models.Model):
    """Django data model Admin"""
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Staff(models.Model):
    """Django data model Admin"""
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SemiAdmin(models.Model):
    """Django data model Admin"""
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AdminHOD(models.Model):
    """Django data model Admin"""
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Teacher(models.Model):
    """Django data model Teacher"""
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    """Django data model Course"""
    course_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.course_name)


class Subject(models.Model):
    """Django data model Subject"""
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.subject_name)


class Student(models.Model):
    """Django data model Student"""
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    gender = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="SM_app/students")
    address = models.TextField()
    course_id = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    session_start_year = models.DateField(blank=True, null=True)
    session_end_year = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.admin.first_name)


class Attendance(models.Model):
    """Django data model Attendance"""
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    attendance_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.attendance_date)


class AttendanceReport(models.Model):
    """Django data model AttendanceReport"""
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.student_id)


class LeaveReportStudent(models.Model):
    """Django data model LeaveReportStudent"""
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    leave_date = models.DateTimeField()
    leave_message = models.TextField(blank=True)
    leave_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.student_id.admin.first_name)


class LeaveReportTeacher(models.Model):
    """Django data model LeaveReportTeacher"""
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    leave_date = models.DateTimeField()
    leave_message = models.TextField(blank=True)
    leave_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.teacher_id.admin.first_name)


class FeedbackStudent(models.Model):
    """Django data model FeedbackStudent"""
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True)
    feedback_reply = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.name)


class FeedbackTeacher(models.Model):
    """Django data model FeedbackTeacher"""
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True)
    feedback_reply = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.name)


class NotificationStudent(models.Model):
    """Django data model NotificationStudent"""
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.name)


class NotificationTeacher(models.Model):
    """Django data model NotificationTeacher"""
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.name)


# Creating signal
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Teacher.objects.create(admin=instance)
        if instance.user_type == 3:
            Student.objects.create(admin=instance, course_id=Course.objects.get(id=1))
            # Student.objects.create(admin=instance, course_id=Course.objects.get(id=1))
        if instance.user_type == 4:
            Parent.objects.create(admin=instance)
        if instance.user_type == 5:
            Staff.objects.create(admin=instance)
        if instance.user_type == 6:
            SemiAdmin.objects.create(admin=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.teacher.save()
    if instance.user_type == 3:
        instance.student.save()
    if instance.user_type == 4:
        instance.parent.save()
    if instance.user_type == 5:
        instance.staff.save()
    if instance.user_type == 6:
        instance.semiadmin.save()
