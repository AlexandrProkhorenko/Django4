from django.contrib import admin

from .models import Student, Teacher, StudentPosition


class StudentPositioninline(admin.TabularInline):
    model = StudentPosition


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    inlines = [StudentPositioninline, ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    inlines = [StudentPositioninline, ]
