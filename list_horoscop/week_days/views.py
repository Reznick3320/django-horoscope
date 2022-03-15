from os import rename
from urllib import response
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

week_days_dict = {
    'monday': 'Список дел Понедельник',
    'tuesday': 'Список дел Вторник',
    'wednesday': 'Список дел Среда',
    'thursday': 'Список дел Четверг',
    'friday': 'Список дел Пятница',
    'saturday': 'Список дел Суббота',
    'sunday': 'Список дел Воскресенье',

}

def index(request):
    days = list(week_days_dict)
    context = {
        'days': days
    }
    return render(request, 'week_days/index.html', context=context)

def get_info_about_week_day(request, sing_day: str):
    description = week_days_dict.get(sing_day)
    data = {
        'description_days': description,
        'sing': sing_day
    }
    return render(request, 'week_days/info_days.html', context=data)
    
def get_info_about_week_day_bu_number(request, sing_day: int):
    day = list(week_days_dict)
    if sing_day > len(day):
        return HttpResponseNotFound(f'Неверный номер дня - {sing_day}')
    name_day = day[sing_day-1]
    revers_url = reverse('name_day', args=(name_day, ))
    return HttpResponseRedirect(revers_url)
        
