import django_filters
from dashboard.models import Dataset


class DataSetFilters(django_filters.FilterSet):

    class Meta:
        model = Dataset
        fields = {
            'country': ('exact',),
            'channel': ('exact', 'in'),
            'os': ('exact',),
            'date': ('gt', 'lt', 'exact', 'gte', 'lte',)
        }
