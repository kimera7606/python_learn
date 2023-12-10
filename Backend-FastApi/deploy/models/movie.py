from config.database import base
from sqlalchemy import Column, Integer
class Movie(base):
    __tablename__ = "movies"