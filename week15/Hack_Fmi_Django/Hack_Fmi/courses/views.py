from django.shortcuts import render
from .models import Course

# Create your views here.


def create_course(request):
    if request.method == 'POST':
        name = request.POST.get('course_name')
        description = request.POST.get('course_description')
        startd = request.POST.get('course_start')
        endd = request.POST.get('course_end')

        Course.objects.create(name=name,
                              description=description,
                              start_date=startd,
                              end_date=endd)

    return render(request, 'create_course.html', locals())


def detail_course(request, *args, **kwargs):
    name = kwargs['course']
    descr = Course.objects.get(name=name).description
    return render(request, "detail_course.html", locals())


def edit_course(request, *args, **kwargs):
    if request.method == 'POST':
        pass
    return render(request, 'edit_course.html', locals())
