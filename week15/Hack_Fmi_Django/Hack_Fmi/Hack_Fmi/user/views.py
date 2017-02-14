from django.shortcuts import render, redirect
from django.urls import reverse
from Hack_Fmi.user.models import User
from passlib.hash import pbkdf2_sha256
from django.http import HttpResponse

# Create your views here.


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if not User.exists(email):
            password = pbkdf2_sha256.hash(password)
            user = User(email=email, password=password)
            user.save()
            return redirect(reverse('index'))
        else:
            return HttpResponse('Сорри Мотори Този Юзър съществува!')

    return render(request, 'register.html', locals())


def login(request):
    request.session['email'] = None
    session_email = request.session.get('email', False)
    # import ipdb; ipdb.set_trace()
    if session_email:
        return redirect(reverse('profile'))
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        u = User.user_login(email=email, password=password)

        if not u:
            # return HttpResponse('Сорри Мотори - Wrong user/pass')
            err_mssg = 'Сорри Мотори - Wrong user/pass'
        else:
            request.session['email'] = email
            response = redirect(reverse('profile'))

    return render(request, 'login.html', locals())


def profile(request):
    email = request.session['email']
    return render(request, 'profile.html', locals())
