from os import environ as E

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_CONFIG = {
   key: E[f'DB{key}'] for key in ['SCHEMA', 'USER', 'PASS', 'HOST', 'PORT', 'NAME']
}
DB_URI_TEMPLATE = '{SCHEMA}://{USER}:{PASS}@{HOST}:{PORT}/{NAME}'
MYSQL_DATABASE_URL = DB_URI_TEMPLATE.format(**DB_CONFIG)

engine = create_engine(MYSQL_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
