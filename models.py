from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TypeOfBusiness(Base):
    __tablename__ = 'type_of_buisness'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    code = Column(String(255), nullable=False, index=True)
    parent_code = Column(String(255), nullable=False)
    section = Column(String(255), nullable=False)
    name = Column(String(1024), nullable=False)
    comment = Column(String)

