from django.shortcuts import render
from .models import Student

def students_list(request):
    template = 'school/students_list.html'
    # Получаем всех учеников из базы данных
    students = Student.objects.all()
    
    # Передаем учеников в контекст шаблона
    context = {
        'object_list': students
    }
    
    return render(request, template, context)