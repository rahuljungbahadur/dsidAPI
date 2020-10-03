from sqlalchemy import Boolean, Column, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

class Ingredient(Base):
    __tablename__ = "calculator"

    ##Columns from the table
    keyVal = Column(Integer, primary_key=True)
    version = Column(Integer)
    product = Column(Integer)
    id = Column(Integer)
    name = Column(String)
    label = Column(Float)
    unit = Column(String)
    min = Column(Float)
    max = Column(Float)
    step = Column(Integer)
    syn = Column(String)
    ## Parameter Estimates
    pm0 = Column(Float)
    pm1 = Column(Float)
    pm2 = Column(Float)

    ## Standard Error of mean Estimates
    sem0 = Column(Float)
    sem1 = Column(Float)
    sem2 = Column(Float)
    sem3 = Column(Float)
    sem4 = Column(Float)
    sem5 = Column(Float)
    sem6 = Column(Float)
    sem7 = Column(Float)
    sem8 = Column(Float)
    sem9 = Column(Float)

    ## Standard error of observations Estimate
    seo0 = Column(Float)
    seo1 = Column(Float)
    seo1 = Column(Float)
    seo2 = Column(Float)
    seo3 = Column(Float)
    seo4 = Column(Float)
    seo5 = Column(Float)
    seo6 = Column(Float)

    ## Lower 95%CI Estimates
    LI95_0 = Column(Float)
    LI95_1 = Column(Float)
    LI95_2 = Column(Float)
    LI95_3 = Column(Float)
    LI95_4 = Column(Float)
    LI95_5 = Column(Float)
    LI95_6 = Column(Float)
    LI95_7 = Column(Float)
    LI95_8 = Column(Float)
    LI95_9 = Column(Float)

    ## Upper 95% Ci Estimates
    UI95_0 = Column(Float)
    UI95_1 = Column(Float)
    UI95_2 = Column(Float)
    UI95_3 = Column(Float)
    UI95_4 = Column(Float)
    UI95_5 = Column(Float)
    UI95_6 = Column(Float)
    UI95_7 = Column(Float)
    UI95_8 = Column(Float)
    UI95_9 = Column(Float)

