from typing import Tuple
import psycopg2
import os


def get_connection():
    conn = psycopg2.connect(database=os.getenv("DBNAME"),
                            host="localhost",
                            user=os.getenv("DBUSER"),
                            password=os.getenv("DBPW"),
                            port=5432)

    return conn


def create_accounts_from_json(filepath) -> None:
    pass
