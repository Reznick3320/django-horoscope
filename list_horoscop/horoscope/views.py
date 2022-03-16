from django.shortcuts import redirect, render
from django.http import HttpResponse
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
    zodiacs = list(zodiac_gict)
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context)

def get_info_about_sing_zodiac(request, sing_zodiak):
    description = zodiac_gict.get(sing_zodiak)
    zodiacs = list(zodiac_gict)
    data = {
        'description_zodiac': description,
        'sing': sing_zodiak.title(),
        'sing_name': description.split()[0],
        'zodiacs': zodiacs,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)