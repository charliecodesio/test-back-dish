import logging
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from .secrets import get_secret

# Load environment variables
ENV = os.getenv("ENV", "dev")

if ENV == "dev":
    from dotenv import load_dotenv
    load_dotenv()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Get secret names from environment
REGION = os.getenv("AWS_REGION")
print('REGION -------> ', REGION)
DB_CREDENTIALS_SECRET = os.getenv("DB_CREDENTIALS_SECRET")
print('DB_CREDENTIALS_SECRET -------> ', DB_CREDENTIALS_SECRET)
DB_CONFIG_SECRET = os.getenv("DB_CONFIG_SECRET")
print('DB_CONFIG_SECRET -------> ', DB_CONFIG_SECRET)
try:
    credentials = get_secret(DB_CREDENTIALS_SECRET, REGION)
    print('credentials -------> ',credentials)
    config = get_secret(DB_CONFIG_SECRET, REGION)
    print('config -------> ',config)
    username = credentials["username"]
    password = credentials["password"]
    host = config["host"]
    port = config["port"]
    dbname = config["dbname"]

    DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{dbname}"
    logger.info("Successfully constructed the database URL from secrets.")

except Exception as e:
    logger.error(f"Failed to retrieve database configuration: {e}")
    raise RuntimeError("Could not retrieve or build the database connection URL.")

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    Base = declarative_base()
    logger.info("Database engine successfully created.")
except SQLAlchemyError as db_error:
    logger.error(f"Error connecting to the database: {db_error}")
    raise RuntimeError("Failed to connect to the database.")
