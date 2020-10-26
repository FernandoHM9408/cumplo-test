# Cumplo-test

Prueba tecnica para cumplo

# Prerequisitos

- [Docker](https://docs.docker.com/install/)
- [Docker-Compose](https://docs.docker.com/compose/)
- [Token de Banxico](https://www.banxico.org.mx/SieAPIRest/service/v1/token)

*Nota*
- Una vez que se tenga el valor de un token de banxico (https://www.banxico.org.mx/SieAPIRest/service/v1/token), se debe establecer el valor dentro del archivo .env para la varieble BANXICO_TOKEN, el archivo .env esta en la raiz del proyecto


# Inicializar el proyecto

Correr el proyecto en local:

```bash
docker-compose up
```

Esperar hasta el mensaje, para empezar a usar el proyecto

```bash
App running at:
- Local:   http://localhost:8080/
```

El [backend](localhost:8000/admin/) corre en ```localhost:8000/admin/```

El [frontend](localhost:8080) (la aplicacion) corre en ```localhost:8080```

La [documentacion](localhost:8081) de la api corre en ```localhost:8001```

**[Documentacion de la API](backend/docs/api/currencies.md)**
