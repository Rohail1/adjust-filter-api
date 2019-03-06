from django.db.models import F
from rest_framework import viewsets, mixins, status
from rest_framework.exceptions import ValidationError
from django.db.models import Sum
from dashboard.models import Dataset
from dashboard.serializers import DataSetSerializer, AggregatedDataSetSerializer
from dashboard.filters import DataSetFilters


class DataSetListView(mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    def get_queryset(self):
        qs = Dataset.objects.all()

        if self.request.GET.get('group_by'):
            group_by = self.request.GET.get('group_by').split(',')
            for group in group_by:
                if not hasattr(Dataset, group):
                    raise ValidationError({'message': 'Bad Request. %s is not a valid column.' % group})
            qs = qs.values(*group_by).annotate(installs=Sum('installs'), impressions=Sum('impressions'),
                                               clicks=Sum('clicks'), spend=Sum('spend'),
                                               revenue=Sum('revenue'),)
        if self.request.GET.get('order_by'):
            order_by = self.request.GET.get('order_by').split(',')
            for order in order_by:
                order = order.replace('-', '')
                if not hasattr(Dataset, order):
                    raise ValidationError({'message': 'Bad Request. %s is not a valid column.' % order})
            qs = qs.order_by(*order_by)
        return qs

    def get_serializer_class(self):
        if self.request.GET.get('group_by'):
            return AggregatedDataSetSerializer
        else:
            return DataSetSerializer

    filterset_class = DataSetFilters

