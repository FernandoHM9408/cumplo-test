from django.urls import path
from apps.series.api.v1.views import UDIAPIView



urlpatterns = [
    path('currency/<str:currency>/<str:init_date>/<str:end_date>', UDIAPIView.as_view()),
]
