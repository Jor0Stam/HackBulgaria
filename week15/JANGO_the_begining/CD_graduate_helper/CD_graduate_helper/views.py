# from django.http import HttpResponse
from django.shortcuts import render
from do_math import get_factoriel, get_fibonaci
from do_math import get_n_primes


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
        fiboanci = ""
    else:
        fiboanci = get_fibonaci(int(request.POST.get('fibonaci_input', None)))
    return render(request, "index.html", locals())


def nth_prime(request):
    if not request.POST.get('prime_input', None):
        nPrimes = ""
    else:
        nPrimes = get_n_primes(int(request.POST.get('prime_input', None)))
    return render(request, "index.html", locals())
