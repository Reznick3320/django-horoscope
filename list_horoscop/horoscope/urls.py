from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('', views_horoscope.index, name='horoscope_index'),
    path('<str:sing_zodiak>', views_horoscope.get_info_about_sing_zodiac, name='horoscope_name'),
]
