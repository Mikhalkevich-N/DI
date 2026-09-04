from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_list, name='home'),  # Главная страница (пустой путь)
    path('students/', views.students_list, name='students'),  # Страница списка учеников
]