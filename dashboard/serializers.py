from rest_framework import serializers
from dashboard.models import Dataset


class DataSetSerializer(serializers.ModelSerializer):

    cpi = serializers.FloatField(source='get_cpi')

    class Meta:
        model = Dataset
        fields = "__all__"


class AggregatedDataSetSerializer(serializers.Serializer):

    date = serializers.DateField(required=False)
    channel = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    os = serializers.CharField(required=False)
    impressions = serializers.IntegerField()
    installs = serializers.IntegerField()
    clicks = serializers.IntegerField()
    spend = serializers.DecimalField(max_digits=12, decimal_places=2)
    revenue = serializers.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        fields = "__all__"
