from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    context = {}
    template = 'school/students_list.html'
    ordering = 'group'
    context['object_list'] = Student.objects.order_by(ordering).prefetch_related('teacher')

    return render(request, template, context)
