import boto3
import json
import logging

logger = logging.getLogger(__name__)

def get_secret(secret_name: str, region_name: str = "us-east-1") -> dict:
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)
    print(f"Retrieving secret: {secret_name} from region: {region_name}")
    print(f"Using AWS Secrets Manager client: {client}")
    try:
        response = client.get_secret_value(SecretId=secret_name)
        print(f"Response from Secrets Manager: {response}")
    except client.exceptions.ResourceNotFoundException:
        logger.error(f"Secret '{secret_name}' not found.")
        raise
    except client.exceptions.InvalidRequestException as e:
        logger.error(f"Invalid request: {e}")
        raise
    except client.exceptions.InvalidParameterException as e:
        logger.error(f"Invalid parameter: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error retrieving secret: {e}")
        raise

    if "SecretString" in response:
        try:
            return json.loads(response["SecretString"])
        except json.JSONDecodeError as json_error:
            logger.error(f"Invalid JSON format: {json_error}")
            raise
    else:
        raise ValueError("Secret does not contain a valid SecretString.")
