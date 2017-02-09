from django.shortcuts import render, get_object_or_404
from .models import Lecture
from courses.models import Course

# Create your views here.


def create_lecture(request):
    if request.method == "POST":
        name = request.POST.get('lecture_name')
        week = request.POST.get('lecture_week')
        course = request.POST.get('course_id')
        url = request.POST.get('course_url')
        Lecture.objects.create(name=name,
                               week=week,
                               course=Course.objects.get(id=course),
                               url=url)

    return render(request, 'create_lecture.html', locals())


def detail_lecture(request, *args, **kwargs):
    name = kwargs['lecture']
    lecture_url = get_object_or_404(Lecture, name=name)
    return render(request, 'detail_lecture.html', locals())
