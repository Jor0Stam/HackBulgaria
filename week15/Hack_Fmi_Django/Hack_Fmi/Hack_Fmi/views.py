from django.shortcuts import render
from courses.models import Course


def default(request):
    all_courses = Course.objects.all()
    return render(request, 'index.html', locals())


def handler404(request):
    return render(request, '404.html', locals())
