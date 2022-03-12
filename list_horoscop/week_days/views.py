from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

week_days_dict = {
    'monday': 'Список дел Понедельник',
    'tuesday': 'Список дел Вторник',
    'wednesday': 'Список дел среда',
    'thursday': 'Список дел четверг',
    'friday': 'Список дел пятница',
    'saturday': 'Список дел суббота',
    'sunday': 'Список дел воскресенье',

}

def get_info_about_week_day(request, sing_day: str):
    description = week_days_dict.get(sing_day, None)
    if description:
        return HttpResponse(f'День недели - {sing_day}')
    else:
        return HttpResponseNotFound(f'Нет такого дня недели - {sing_day}')
    
def get_info_about_week_day_bu_number(request, sing_day: int):
    day = list(week_days_dict)
    if sing_day > len(day):
        return HttpResponseNotFound(f'Неверный номер дня - {sing_day}')
    name_day = day[sing_day-1]
    revers_url = reverse('name_day', args=(name_day, ))
    return HttpResponseRedirect(revers_url)
        
