from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User
from passlib.hash import pbkdf2_sha256
from django.http import HttpResponse
from Hack_Fmi.decorators import login_required, annon_required
from Hack_Fmi.courses.views import courses_table
from Hack_Fmi.user.forms import LoginForm, RegisterForm

# Create your views here.


@annon_required(redirect_url='profile')
def register(request):
    if request.method == 'POST':
        my_form = RegisterForm(request.POST)
        import ipdb; ipdb.set_trace()
        if my_form.is_valid():
            email = my_form.cleaned_data['email']
            password = my_form.cleaned_data['password']
            first_name = my_form.cleaned_data.get('first_name', False)
            last_name = my_form.cleaned_data.get('last_name', False)
            # email = request.POST['email']
            # password = request.POST['password']

            if User.exists(email):
                return HttpResponse('Сорри Мотори Този Юзър съществува!')
            else:
                password = pbkdf2_sha256.hash(password)
                # my_form.save()
                user = User(email=email, password=password)
                user.save()
                return redirect(reverse('login'))
    my_form = RegisterForm()
    return render(request, 'register.html', {'my_form': my_form})


@annon_required(redirect_url='profile')
def login(request):
    session_email = request.session.get('email', False)
    if session_email:
        return redirect(reverse('profile'))
    if request.method == 'POST':
        my_form = LoginForm(request.POST)
        import ipdb; ipdb.set_trace()

        if my_form.is_valid():
            email = my_form.cleaned_data['email']
            password = my_form.cleaned_data['password']

            usr = User.user_login(email=email, password=password)

        # import ipdb; ipdb.set_trace()
            if not usr:
                err_mssg = 'Сорри Мотори - Wrong user/pass'
            else:
                request.session['email'] = email
                return redirect(reverse('profile'))
    my_form = LoginForm()
    import ipdb; ipdb.set_trace()
    return render(request, 'login.html', {'my_form': my_form})# locals())


@login_required(redirect_url='login')
def profile(request):
    email = request.session['email']
    return render(request, 'profile.html', locals())


def logout(request):
    # import ipdb; ipdb.set_trace()
    request.session.flush()
    return courses_table(request)
