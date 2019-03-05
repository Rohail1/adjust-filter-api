from django.conf.urls import url
from dashboard.views import DataSetListView

urlpatterns = [
    url(r'^data/$', DataSetListView.as_view({
        'get': 'list'
    }))
]
