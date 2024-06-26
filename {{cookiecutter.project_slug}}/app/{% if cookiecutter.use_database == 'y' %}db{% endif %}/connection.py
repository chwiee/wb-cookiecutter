from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


DB_URL = os.environ['DB_URL']

engine = create_engine(DB_URL, pool_pre_ping=True)
Session = sessionmaker()
