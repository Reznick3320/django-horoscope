from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('', views_horoscope.index),
    path('<int:sing_zodiak>', views_horoscope.get_info_about_sing_zodiac_by_number, name='horoscope_name'),
    path('<str:sing_zodiak>', views_horoscope.get_info_about_sing_zodiac, name='horoscope_name'),
]
