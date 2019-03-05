from rest_framework import serializers
from dashboard.models import Dataset


class DataSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dataset
        fields = "__all__"
