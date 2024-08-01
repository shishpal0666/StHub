import os
import psycopg2

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY') or os.urandom(12).hex()
    DATABASE = {
        'name': 'StHub',
        'user': 'postgres',
        'password': 'password',
        'host': 'localhost',
        'port': 5432
    }