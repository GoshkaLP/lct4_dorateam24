from sqlalchemy import Column, Integer, String, Boolean
from geoalchemy2 import Geometry

from backend.utils.db import Base


class Territories(Base):
    __tablename__ = "territories"

    id = Column(Integer, primary_key=True)
    district = Column(String)
    area = Column(String)
    cadastral = Column(String)
    address = Column(String)
    square = Column(Integer)
    geometry = Column(Geometry("POLYGON"))
    is_zpo = Column(Boolean)
    is_msk = Column(Boolean)


class Districts(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True)
    district = Column(String)


class Areas(Base):
    __tablename__ = "areas"

    id = Column(Integer, primary_key=True)
    area = Column(String)


class Cadastrals(Base):
    __tablename__ = "cadastrals"

    id = Column(Integer, primary_key=True)
    cadastral = Column(String)


class Addresses(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    address = Column(String)
