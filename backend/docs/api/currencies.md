# Tipos de cambio
Obtener informacion de tipos de cambio, en especifico de UDI's, USD y TIIE


## Obetener informacion de tipo de cambio

**Request**:

`GET` `/api/series/currency/:currency_name/:init_data/:end_date

Parametros:

Nombre           | Requerido | Descripcion
-----------------|---------- |------------
currency_name    | Si        | El nombre del tipo de cambio (puede ser UDI, USD o TIIE).
init_data        | Si        | El rango de fecha inicial para la busqueda.
end_date         | Si        | El rango de fecha final para la busqueda.


Notas:

- **Si no se pone fecha inicial ni final se tomara el dia actual para las dos fechas**
- **No requiere de ningun tipo de autentificacion o autorizacion**

**Response (con UDI)**:


```json
http://localhost:8000/api/series/currency/USD/2020-09-28/2020-10-02
Content-Type application/json
200 Ok

{
    "valores": [
        {
            "fecha": "28/09/2020",
            "dato": "22.4573"
        },
        {
            "fecha": "29/09/2020",
            "dato": "22.3598"
        },
        {
            "fecha": "30/09/2020",
            "dato": "22.1438"
        },
        {
            "fecha": "01/10/2020",
            "dato": "21.9562"
        },
        {
            "fecha": "02/10/2020",
            "dato": "21.7025"
        }
    ],
    "promedio": 22.12392,
    "max": 22.4573,
    "min": 21.7025
}
```

**Response (con UDI)**:


```json
http://localhost:8000/api/series/currency/UDI/2020-09-28/2020-10-02
Content-Type application/json
200 Ok

{
    "valores": [
        {
            "fecha": "28/09/2020",
            "dato": "6.548157"
        },
        {
            "fecha": "29/09/2020",
            "dato": "6.548868"
        },
        {
            "fecha": "30/09/2020",
            "dato": "6.549579"
        },
        {
            "fecha": "01/10/2020",
            "dato": "6.550290"
        },
        {
            "fecha": "02/10/2020",
            "dato": "6.551002"
        }
    ],
    "promedio": 6.549579199999999,
    "max": 6.551002,
    "min": 6.548157
}
```

**Response (con TIIE)**:


```json
http://localhost:8000/api/series/currency/TIE/2020-09-28/2020-10-02
Content-Type application/json
200 Ok

[
    {
        "idSerie": "SF331451",
        "titulo": "TIIE de Fondeo a Un Día Hábil Bancario, Mediana ponderada por volumen",
        "datos": [
            {
                "fecha": "28/09/2020",
                "dato": "4.25"
            },
            {
                "fecha": "29/09/2020",
                "dato": "4.30"
            },
            {
                "fecha": "30/09/2020",
                "dato": "4.28"
            },
            {
                "fecha": "01/10/2020",
                "dato": "4.24"
            },
            {
                "fecha": "02/10/2020",
                "dato": "4.24"
            }
        ]
    },
    {
        "idSerie": "SF43783",
        "titulo": "TIIE a 28 días Tasa de interés en por ciento anual",
        "datos": [
            {
                "fecha": "28/09/2020",
                "dato": "4.5605"
            },
            {
                "fecha": "29/09/2020",
                "dato": "4.5500"
            },
            {
                "fecha": "30/09/2020",
                "dato": "4.5495"
            },
            {
                "fecha": "01/10/2020",
                "dato": "4.5485"
            },
            {
                "fecha": "02/10/2020",
                "dato": "4.5487"
            }
        ]
    },
    {
        "idSerie": "SF43878",
        "titulo": "Tasas de interés interbancarias                Por ciento anual TIIE a 91 días",
        "datos": [
            {
                "fecha": "28/09/2020",
                "dato": "4.5600"
            },
            {
                "fecha": "29/09/2020",
                "dato": "4.5550"
            },
            {
                "fecha": "30/09/2020",
                "dato": "4.5530"
            },
            {
                "fecha": "01/10/2020",
                "dato": "4.5525"
            },
            {
                "fecha": "02/10/2020",
                "dato": "4.5512"
            }
        ]
    }
]
```




