import os

from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from .models import Base

load_dotenv(find_dotenv(usecwd=True))

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    print('Ошибка токена')
    exit(1)
    
def get_enginge():
    return create_engine(
        DATABASE_URL,
        connect_args={'connect_timeout': 5},
        poolclass=NullPool
    )

def create_tables():
    engine = get_enginge()
    Base.metadata.create_all(engine)

def get_session():
    engine = get_enginge()
    return sessionmaker(bind=engine)()