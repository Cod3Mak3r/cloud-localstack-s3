# Proyecto LocalStack - Simulación de Servicios AWS

Este proyecto tiene como objetivo simular los servicios de Amazon Web Services (AWS) de manera local utilizando **LocalStack**. LocalStack proporciona un entorno para desarrollar y probar aplicaciones de AWS sin necesidad de utilizar la nube real de AWS.

## **Requisitos Previos**

- **Docker** instalado en tu máquina. [Instrucciones de instalación de Docker](https://www.docker.com/get-started)
- **Docker Compose** para gestionar contenedores. [Instrucciones de instalación de Docker Compose](https://docs.docker.com/compose/install/)
- **Git** para clonar el repositorio y gestionar el código. [Instrucciones de instalación de Git](https://git-scm.com/)

## **Configuración y Ejecución**

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu-usuario/localstack-s3.git
    cd localstack-s3
    ```

2. Asegúrate de que el archivo `docker-compose.yml` esté configurado correctamente.

3. Ejecuta LocalStack con Docker Compose:

    ```bash
    docker-compose up -d
    ```

4. Verifica que el contenedor esté corriendo:

    ```bash
    docker ps
    ```

5. Interactúa con los servicios simulados, como S3, DynamoDB, y SQS, utilizando la API de LocalStack.

### **Ejemplo de Código de Uso**

Aquí tienes algunos ejemplos de cómo interactuar con los servicios simulados de LocalStack usando Python y **boto3**.

#### **Subir un archivo a S3**
```python
import boto3

# Crear un cliente S3
s3 = boto3.client('s3', endpoint_url="http://localhost:4566")

# Crear un bucket y subir un archivo
s3.create_bucket(Bucket="mi-bucket")
s3.upload_file("archivo.txt", "mi-bucket", "archivo.txt")
