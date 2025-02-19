from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EvenWeek(Base):
    __tablename__ = 'even_week'

    id = Column(Integer, primary_key=True)
    week_day = Column(String)
    first_pair = Column(String)
    second_pair = Column(String)
    third_pair = Column(String)
    fourth_pair = Column(String)
    fifth_pair = Column(String)

class OddWeek(Base):
    __tablename__ = 'odd_week'

    id = Column(Integer, primary_key=True)
    week_day = Column(String)
    first_pair = Column(String)
    second_pair = Column(String)
    third_pair = Column(String)
    fourth_pair = Column(String)
    fifth_pair = Column(String)

class WeekDeterminant(Base):
    __tablename__ = 'week_determinant'

    id = Column(Integer, primary_key=True)
    week_date = Column(String)
    week_counter = Column(Integer)