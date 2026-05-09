from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class NewsSource(Base):
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String, unique=True)
    rss_url = Column(String, nullable=True)
    last_scraped = Column(DateTime)

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String, unique=True)
    description = Column(String)
    pub_date = Column(DateTime)
    source_id = Column(Integer)