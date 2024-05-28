from langchain_core.embeddings import Embeddings
from langchain_postgres import PGVector

import settings

DB_CONNECTION_STRING = PGVector.connection_string_from_db_params(
    driver=settings.DATABASE_DRIVER,
    host=settings.DATABASE_HOST,
    port=settings.DATABASE_PORT,
    user=settings.DATABASE_USER,
    password=settings.DATABASE_PASSWD,
    database=settings.DATABASE_NAME
)

def get_db_connection(embeddings: Embeddings, *args, **kwargs) -> PGVector:
    return PGVector(
        embeddings=embeddings,
        connection=DB_CONNECTION_STRING,
        *args,
        **kwargs
    )
