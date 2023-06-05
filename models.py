from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class TypeOfBusiness(Base):
    __tablename__ = 'type_of_buisness'

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    code = Column(String(255), nullable=False, unique=True)
    parent_code = Column(String(255), nullable=False)
    section = Column(String(255), nullable=False)
    name = Column(String(1024), nullable=False)
    comment = Column(String)
    companies = relationship('Company')


class Company(Base):
    __tablename__ = 'company'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    name = Column(String(1024), nullable=False)
    full_name = Column(String(1024), nullable=False)
    inn = Column(String(255), nullable=False)
    kpp = Column(String(255), nullable=False)
    # okved = Column(String(255), nullable=False)
    okved = Column(String(255), ForeignKey('type_of_buisness.code'))
