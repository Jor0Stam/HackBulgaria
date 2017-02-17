from passlib.hash import pbkdf2_sha256
from django.shortcuts import redirect
from django.urls import reverse
from functools import wraps


def encrypt_pass(f):
    def wrapper(*args, **kwargs):
        kwargs['password'] = pbkdf2_sha256.hash(kwargs['password'])
        return kwargs
    return wrapper


def annon_required(**dkwargs):  # redirect_url='profile'
    def wrapper(f):
        @wraps(f)
        def accepter(request, *args, **kwargs):
            # import ipdb; ipdb.set_trace()
                session_email = request.session.get('email', False)
                if session_email:
                    return redirect(reverse(dkwargs['redirect_url']))
                return f(request, *args, **kwargs)
        return accepter
    return wrapper


def login_required(**dkwargs):  # redirect_url='login'
    def wrapper(f):
        @wraps(f)
        def accepter(request, *args, **kwargs):
            # import ipdb; ipdb.set_trace()
            session_email = request.session.get('email', False)
            if session_email:
                return f(request, *args, **kwargs)
            return redirect(reverse(dkwargs['redirect_url']))
        return accepter
    return wrapper

# >>> # verifying the password
# >>> pbkdf2_sha256.verify("toomanysecrets", hash)
# True
# >>> pbkdf2_sha256.verify("joshua", hash)
# False
