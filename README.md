
# Proyecto gRPC con Docker

Este proyecto demuestra la comunicación entre un servidor y un cliente utilizando el protocolo gRPC. Ambos, el servidor y el cliente, están contenerizados usando Docker y se comunican entre sí utilizando diferentes métodos gRPC.

## Pre-requisitos

- Docker y Docker Compose instalados en tu máquina.
- Acceso a la terminal o línea de comandos.

## Configuración y despliegue

1. **Clonar el repositorio**:
   \```
   git clone [URL-del-repositorio]
   cd [nombre-del-directorio]
   \```

2. **Otorgar permisos de ejecución al script**:
   ```bash
   chmod +x run.sh
   ```

3. **Ejecutar el script**:
   ```bash
   ./run.sh
   ```

   El script `run.sh` se encarga de construir las imágenes Docker y de iniciar los contenedores para el servidor y el cliente gRPC.

## Servicios Implementados

El servidor gRPC implementa los siguientes métodos:

1. **SayHelloSimple**: Un método unario que recibe un nombre y devuelve un saludo.
   
2. **SayHelloServerStream**: Un método de streaming del servidor que envía múltiples saludos al cliente.
   
3. **SayHelloClientStream**: Un método de streaming del cliente que recibe múltiples nombres y devuelve un saludo conjunto.
   
4. **SayHelloBidirectional**: Un método de streaming bidireccional donde el cliente envía múltiples nombres y el servidor devuelve un saludo para cada nombre recibido.

## Salida esperada

Cuando ejecutes el proyecto, deberías ver una serie de mensajes en la terminal que indican que el cliente ha recibido respuestas del servidor. Estos mensajes corresponden a las respuestas de los diferentes métodos gRPC implementados en el servidor.

## Limpieza

Después de ejecutar el proyecto, puedes detener y eliminar los contenedores usando:

```bash
docker-compose down
```

## Problemas conocidos

1. Si ves un error que indica que el puerto `50051` ya está en uso, puedes detener el proceso que está utilizando ese puerto o modificar el archivo `docker-compose.yml` para mapear un puerto diferente.

2. Si experimentas problemas con la resolución de nombres en Docker, asegúrate de que ambos contenedores, cliente y servidor, se estén ejecutando y que el servidor se haya iniciado correctamente.
