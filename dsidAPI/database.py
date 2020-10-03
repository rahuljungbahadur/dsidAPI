from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

## Change username and password below
user = "root"
pwd = ""
ipAdd = "localhost"
dbName = "new_calculators"

databaseURL = "mysql+mysqlconnector://"+user+":"+pwd+"@"+ipAdd+"/"+dbName

## Create Engine
dbEngine = create_engine(databaseURL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=dbEngine)

Base = declarative_base()