import boto3

# Configurar conexión a LocalStack (endpoint simulado)
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",  # Endpoint de LocalStack
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
)

BUCKET_NAME = "mi-bucket-simulado"

def crear_bucket():
    """Crea un bucket en LocalStack."""
    s3.create_bucket(Bucket=BUCKET_NAME)
    print(f"✅ Bucket '{BUCKET_NAME}' creado con éxito.")

def subir_archivo():
    """Sube un archivo al bucket simulado."""
    archivo = "test.txt"
    with open(archivo, "w") as f:
        f.write("Este es un archivo de prueba en S3 simulado.")

    s3.upload_file(archivo, BUCKET_NAME, "test.txt")
    print(f"📤 Archivo '{archivo}' subido correctamente.")

def listar_archivos():
    """Lista los archivos dentro del bucket."""
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    if "Contents" in response:
        for obj in response["Contents"]:
            print(f"📄 {obj['Key']}")
    else:
        print("📂 El bucket está vacío.")

def descargar_archivo():
    """Descarga un archivo del bucket."""
    s3.download_file(BUCKET_NAME, "test.txt", "descargado.txt")
    print("📥 Archivo 'test.txt' descargado como 'descargado.txt'.")

if __name__ == "__main__":
    crear_bucket()
    subir_archivo()
    listar_archivos()
    descargar_archivo()
