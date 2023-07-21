import os
from minio import Minio
from minio.error import S3Error as ResponseError

minio_endpoint = "http://159.65.199.5:9090"
minio_access_key = "Biighunter"
minio_secret_key = "11236939.Smh"
minio_bucket_name = "music"

file_path = "./upload-files/*"
object_name = "Enjoy"
def upload_file_to_minio(file_path, object_name):
    try:
        minio_client = Minio(minio_endpoint, access_key=minio_access_key, secret_key=minio_secret_key, secure=False)

        if not minio_client.bucket_exists(minio_bucket_name):
            minio_client.make_bucket(minio_bucket_name)

        minio_client.fput_object(minio_bucket_name, object_name, file_path)

        print(f"File '{object_name}' uploaded successfully to MinIO!")
    except ResponseError as err:
        print(f"MinIO error occurred: {err}")
