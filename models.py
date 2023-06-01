from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TypeOfBusiness(Base):
    __tablename__ = 'type_of_buisness'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False, unique=True, index=True)
    parent_code = Column(String, nullable=False)
    section = Column(String, nullable=False)
    name = Column(String, nullable=False)
    comment = Column(String, nullable=False)

