from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from dashboard.models import Dataset
from dashboard.serializers import DataSetSerializer


class DataSetListView(mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    queryset = Dataset.objects.all()
    serializer_class = DataSetSerializer
    # def list(self, request, *args, **kwargs):
    #     return Response(
    #         data={'status': 'ok'}
    #     )
