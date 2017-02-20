from django.shortcuts import render, redirect
from django.urls import reverse
from Hack_Fmi.courses.models import Course
from .forms import CreateCourseForm  # , EditCourseForm
from .forms2 import EditCourse

# Create your views here.


def courses_table(request):
    all_courses = Course.objects.all()
    return render(request, 'index.html', locals())


def create_course(request):
    if request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('course_name')
            description = form.cleaned_data.get('course_description')
            startd = form.cleaned_data.get('course_start')
            endd = form.cleaned_data.get('course_end')

            Course.objects.create(name=name,
                                  description=description,
                                  start_date=startd,
                                  end_date=endd)

            return redirect(reverse('index'))

    form = CreateCourseForm()
    return render(request, 'create_course.html', locals())


def detail_course(request, *args, **kwargs):
    name = kwargs['course']
    descr = Course.objects.get(name=name).description
    return render(request, "detail_course.html", locals())


def edit_course(request, *args, **kwargs):
    if request.method == 'POST':
        form = EditCourse()
        # if form.is_valid():
        #     # import ipdb; ipdb.set_trace()
        #     old_obj = Course.objects.get(
        #         name=form.cleaned_data.get('old_name'))
        #     for key, value in form.cleaned_data.items():
        #         if value and (key != 'old_name'):
        #             exec("old_obj.{k} = '{v}'".format(k=key, v=value))
        #     old_obj.save()

    form = EditCourse()
    return render(request, 'edit_course.html', locals())
