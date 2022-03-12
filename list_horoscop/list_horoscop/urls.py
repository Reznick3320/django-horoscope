"""list_horoscop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from week_days import urls as urls_week_days
from horoscope import urls as urls_horoscope
from geometry import urls as urls_geometry



urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/', include(urls_horoscope)),
    path('todo_week/', include(urls_week_days)),
    path('calculate_geometry/', include(urls_geometry)),
]
