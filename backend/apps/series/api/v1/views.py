import requests
import json
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from apps.series.utils import get_currency_value, calculate_currency_data


class UDIAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, currency=None, init_date=None, end_date=None):
        currency_data = get_currency_value(currency, init_date, end_date)
        if currency_data:
            if currency != 'TIIE':
                data_currency_converted, promedio, max_value, min_value = calculate_currency_data(currency_data)
                return Response(status=200, data={"valores": data_currency_converted,
                                                 "promedio": promedio,
                                                 "max": max_value,
                                                 "min": min_value})
            return Response(status=200, data=currency_data['bmx']['series'])
        else:
            return Response(status=404, data={'error': 'tipo de cambio no valido'})
