from django.urls import path, include
from apps.series.api.v1 import urls as seriesURLS

urlpatterns = [
    path('series/', include(seriesURLS)),
]
