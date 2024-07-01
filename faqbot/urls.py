# faqbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_answer/', views.get_answer, name='get_answer'),
]
