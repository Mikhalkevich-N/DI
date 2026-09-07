from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter  # импортируем наш фильтр (шаг 2)
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


# Класс для проверки авторства
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешаем чтение (GET, HEAD, OPTIONS) всем
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Разрешаем изменение/удаление только автору
        return obj.creator == request.user


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    # Подключаем наш класс фильтрации (шаг 2)
    filterset_class = AdvertisementFilter

    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_permissions(self):
        """Получение прав для действий."""
        # Для создания, обновления и удаления требуется авторизация
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        # Для просмотра авторизация не требуется
        return []
    
    # Переопределяем метод для проверки прав на конкретный объект
    def check_object_permissions(self, request, obj):
        super().check_object_permissions(request, obj)
        # Если действие - изменение или удаление, проверяем авторство
        if self.action in ["update", "partial_update", "destroy"]:
            permission = IsAuthorOrReadOnly()
            if not permission.has_object_permission(request, self, obj):
                self.permission_denied(request, message="Вы можете изменять или удалять только свои объявления.")

    def perform_create(self, serializer):
        # Автоматически подставляем автора
        serializer.save(creator=self.request.user)