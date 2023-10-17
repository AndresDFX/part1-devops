#!/bin/bash

# Verificar si el puerto 50051 está en uso y, si es así, matar el proceso
if lsof -Pi :50051 -sTCP:LISTEN -t >/dev/null ; then
    echo "El puerto 50051 está en uso. Deteniendo el proceso..."
    kill -9 $(lsof -t -i:50051)
fi

# Construir y ejecutar los contenedores usando docker-compose
docker-compose up --build