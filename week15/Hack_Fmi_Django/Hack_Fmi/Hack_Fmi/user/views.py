from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User
from passlib.hash import pbkdf2_sha256
from django.http import HttpResponse
from Hack_Fmi.decorators import login_required, annon_required
from Hack_Fmi.courses.views import courses_table
# from Hack_Fmi.user.forms import LoginForm

# Create your views here.


@annon_required(redirect_url='profile')
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if User.exists(email):
            return HttpResponse('Сорри Мотори Този Юзър съществува!')
        else:
            password = pbkdf2_sha256.hash(password)
            user = User(email=email, password=password)
            user.save()
            return redirect(reverse('login'))

    return render(request, 'register.html', locals())


# @annon_required(redirect_url='profile')
def login(request='Test'):
    session_email = request.session.get('email', False)
    if session_email:
        return redirect(reverse('profile'))
    # my_form = LoginForm
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        usr = User.user_login(email=email, password=password)

        # import ipdb; ipdb.set_trace()
        if not usr:
            # return HttpResponse('Сорри Мотори - Wrong user/pass')
            err_mssg = 'Сорри Мотори - Wrong user/pass'
        else:
            request.session['email'] = email
            # request.session['user'] = usr
            return redirect(reverse('profile'))


    return render(request, 'login.html', locals())


@login_required(redirect_url='login')
def profile(request):
    email = request.session['email']
    return render(request, 'profile.html', locals())


def logout(request):
    # import ipdb; ipdb.set_trace()
    request.session.flush()
    return courses_table(request)
