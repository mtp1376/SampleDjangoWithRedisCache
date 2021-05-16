from django.core.cache import cache

# Create your views here.
from django.http import HttpResponse


def _factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def _get_cache_key(n):
    return f'factorial({n})'


def factorial_view(request, n):
    if cached_factorial := cache.get(_get_cache_key(n)):
        return HttpResponse(f"{n}! is {cached_factorial}")

    factorial = _factorial(n)
    cache.set(_get_cache_key(n), factorial)
    return HttpResponse(f"{n}! is {factorial}")
