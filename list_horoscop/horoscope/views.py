from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

zodiac_gict = {
    "aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
    "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
    "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
    "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
    "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
    "vigro": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
    "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
    "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
    "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
    "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января)",
    "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
    "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)"
}

def index(request):
    zodiac = list(zodiac_gict)
    li_element = ''
    for sing in zodiac:
        redirect_path = reverse('horoscope_name', args=(sing, ))
        li_element += f"<li><a href='{redirect_path}'>{sing.title()}</a></li>"
    
    response = f"""
    <ol>
        {li_element}
    </ol>

    """
    return HttpResponse(response)

def get_info_about_sing_zodiac(request, sing_zodiak):
    description = zodiac_gict.get(sing_zodiak, None)
    if description:
        return HttpResponse(description)
    else: 
        return HttpResponseNotFound(f'Неизвестный знак зодиака {sing_zodiak}')

def get_info_about_sing_zodiac_by_number(request, sing_zodiak: int):
    zodiak = list(zodiac_gict)
    if sing_zodiak > len(zodiak):
        return HttpResponseNotFound(f'Неизвестный номер знака зодиака {sing_zodiak}')
    name_zodiak = zodiak[sing_zodiak-1]
    redirect_url = reverse('horoscope_name', args=(name_zodiak, ))
    return HttpResponseRedirect(redirect_url)