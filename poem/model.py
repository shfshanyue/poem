# encoding: utf-8

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()


def db_connect():
    return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Phrase (DeclarativeBase):
    __tablename__ = "phrase"

    id = Column(Integer, primary_key=True)
    title = Column('title', String, nullable=True, unique=True)
    author = Column('author', String, nullable=True)
    phrase = Column('phrase', String, nullable=True)
