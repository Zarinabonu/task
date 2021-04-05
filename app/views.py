from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


def task1(self):
    a = [2, 4, 3]
    b = [5, 6, 4]
    result_a = []
    result_b = []
    for ra in reversed(a):
        result_a.append(ra)
    [3, 4, 2]
    for rb in reversed(b):
        result_b.append(rb)
    result_a = int("".join(map(str, result_a)))
    result_b = int("".join(map(str, result_b)))
    result = result_a + result_b
    result = str(result)[::-1]
    result = list(map(str, result))
    print('task 1 : ', result)
    task2(self)
    return HttpResponse(result)


def task2(self):
    new = []
    for i in range(1, 100):
        i = str(i)
        if '0' not in i:
            new.append(i)
    print('task2 :  ', new)
    return new
