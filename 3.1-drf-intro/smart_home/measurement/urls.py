from django.urls import path
from . import views

urlpatterns = [
    # Создать датчик и получить список датчиков
    path('sensors/', views.SensorListCreateView.as_view(), name='sensor-list-create'),
    
    # Получить информацию о датчике и изменить его
    path('sensors/<int:pk>/', views.SensorRetrieveUpdateView.as_view(), name='sensor-detail-update'),
    
    # Добавить измерение
    path('measurements/', views.MeasurementCreateView.as_view(), name='measurement-create'),
]