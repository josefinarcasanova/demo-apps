import ibm_boto3
from ibm_botocore.client import Config, ClientError

from os import environ
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()   

# Sobre las credenciales
# ----------------------
# `bucket_name`               nombre del bucket
# `ibm_api_key_id`            apikey; se encuentra en Service Credentials (apikey).
# ``ibm_service_instance_id`` identificador de la instancia; se encuentra en Service Credentials (resource_instance_id).
# ``endpoint_url``            URL HTTPS del endpoint. NO son los endpoints de Service Credentials. Para más información, ver: https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-endpoints#endpoints-region
# LocationConstraint          es el provisioning code correspondiente al endpoint. Ver: https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-classes#classes-locationconstraint

# Python Credentials Documentation: https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-python#python-credentials
# IBM Cloud Object Storage in Python: https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/ee1d0b44-0fce-4cf6-8545-e1dc961d0668/view?access_token=c0489b861ab65f63be7e3c5ce962003a2a0197660e67ecb140c477c2e11b5fe3

def create_cos_client():
    cos = ibm_boto3.client("s3",
        ibm_api_key_id          =environ['COS_API_KEY_ID'],
        ibm_service_instance_id =environ['COS_INSTANCE_ID'],
        config                  =Config(signature_version="oauth"),
        endpoint_url            =environ['COS_ENDPOINT']
    )
    return cos

def get_cos_file(cos_client, bucket_name, file_name, file_key):
    try:
        if cos_client == None:
            cos_client = create_cos_client()

        if bucket_name == None:
            bucket_name = environ['COS_BUCKET_NAME']

        with open(file_name, 'wb') as file:  
            cos_client.download_file(
                Bucket=bucket_name,
                Key=file_key,
                Filename=file_name
                )
            
            return file
    
    except Exception as e:
        print(Exception, e)