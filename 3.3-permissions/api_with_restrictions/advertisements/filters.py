from django_filters import rest_framework as filters
from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтр для объявлений."""

    # Кастомные фильтры для даты (работают с параметрами created_at__before / created_at__after)
    created_at_before = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    created_at_after = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at_before', 'created_at_after']