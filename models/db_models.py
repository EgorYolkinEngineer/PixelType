from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from core.db_mixins import SerializerMixin

Base = declarative_base()


class Post(Base, SerializerMixin):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    key = Column(String)
    author = Column(String)
    title = Column(String)
    text = Column(String)

    created = Column(Integer)
