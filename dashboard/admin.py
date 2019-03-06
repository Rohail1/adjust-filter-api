from django.contrib import admin
from dashboard.models import Dataset


@admin.register(Dataset)
class DataSetAdmin(admin.ModelAdmin):

    search_fields = ('id', 'country', 'channel', 'os',)
    list_display = ('id', 'date', 'channel', 'country', 'os', 'impressions',  'clicks', 'installs', 'spend', 'revenue')
