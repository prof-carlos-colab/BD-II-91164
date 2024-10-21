from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# URL de conexão para BD MySQL.
DATABASE_URL = f"mysql+pymysql://usuario:senha@host:porta/nome_bd"