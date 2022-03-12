from django.urls import path
from . import views as views_week_days

urlpatterns = [
    path('<int:sing_day>', views_week_days.get_info_about_week_day_bu_number, name='name_day'),
    path('<str:sing_day>', views_week_days.get_info_about_week_day, name='name_day'),
]
