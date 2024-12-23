from sqlalchemy import create_engine



#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Student(Base):
    _tablename_ = 'students'
    
    id=Column(Integer, primary_key=True)
    name =Column(String())

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')
    Base.metadata_create_all(engine)
