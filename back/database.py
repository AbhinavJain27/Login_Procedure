from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url='sqlite:///./login_details.db'
engine=create_engine(url)

SessionLocal=sessionmaker(autoflush=False , autocommit =False , bind=engine)

base=declarative_base()  