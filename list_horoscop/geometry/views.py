from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_rectangle_area(request, width, height):
    s = width * height
    return HttpResponse(f'Площадь прямоугольника - {s}')


def get_square_area(request, width):
    s = width**2
    return HttpResponse(f'Площадь квадрата - {s}')

def get_circle_area(request, radius):
    s = 2*3,14*radius**2
    return HttpResponse(f'Площадь круга - {s}')