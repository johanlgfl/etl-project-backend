import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

load_dotenv()

POSTGRESQL_DATABASE = os.getenv("POSTGRESQL_DATABASE")
POSTGRESQL_USER = os.getenv("POSTGRESQL_USER")
POSTGRESQL_PASSWORD = os.getenv("POSTGRESQL_PASSWORD")
POSTGRESQL_HOST = os.getenv("POSTGRESQL_HOST")
POSTGRESQL_PORT = os.getenv("POSTGRESQL_PORT")

POSTGRESQL_CONNECTION_URI = f"postgresql://{POSTGRESQL_USER}:{POSTGRESQL_PASSWORD}@{POSTGRESQL_HOST}:{POSTGRESQL_PORT}/{POSTGRESQL_DATABASE}"

engine = create_engine(POSTGRESQL_CONNECTION_URI)

meta = MetaData()

conn = engine.connect()
