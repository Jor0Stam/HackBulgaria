# from django.http import HttpResponse
from django.shortcuts import render
from CD_graduate_helper.do_math import *


def index(request):
    # import ipdb; ipdb.set_trace()
    return render(request, 'index.html', locals())


def factoriel(request):
    if request.POST.get('fact_input', None) == "":
        fact = ""
    else:
        fact = get_factoriel(int(request.POST.get('fact_input', None)))
    return render(request, 'index.html', locals())


def fibonaci(request):
    if not request.POST.get('fibonaci_input', None):
        fibo = ""
    else:
        fibo = get_fibonaci(int(request.POST.get('fibonaci_input', None)))
    return render(request, "index.html", locals())


def nth_prime(request):
    if not request.POST.get('prime_input', None):
        nPrimes = ""
    else:
        nPrimes = get_n_primes(int(request.POST.get('prime_input', None)))
    return render(request, "index.html", locals())


def encode(request):
    if not request.POST.get('normal_input', None):
        encoded = ""
    else:
        encoded = encode_rle(request.POST.get('normal_input', None))
    return render(request, 'index.html', locals())


def decode(request):
    if not request.POST.get('encoded_input', None):
        decoded = ""
    else:
        decoded = decode_rle(request.POST.get('encoded_input', None))
    return render(request, 'index.html', locals())
